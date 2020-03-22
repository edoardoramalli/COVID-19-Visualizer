import hashlib
import urllib.request
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np
import argparse


def kmb_formatter(x, pos):
    if pos is not None:
        if x >= 1*10**9:
            return '%1.1fB' % (x * 1e-9)
        elif x >= 1*10**6:
            return '%1.1fM' % (x * 1e-6)
        else:
            return '%1.1fK' % (x * 1e-3)


def file_as_bytes(f):
    with f:
        return f.read()


class Country:
    lat = None
    long = None

    def __init__(self, name, confirmed_case):
        self.name = name
        self.confirmed_case = confirmed_case

    def get_first_data(self, n=0):
        d = list(self.confirmed_case.keys())
        d.sort(key=lambda date: datetime.strptime(date, "%m/%d/%y"))
        for data in d:
            if self.confirmed_case[data] >= n:
                return data

    def ordered_list_confirmed(self, n=0):
        first = self.get_first_data(n)
        d = list(self.confirmed_case.keys())
        d.sort(key=lambda date: datetime.strptime(date, "%m/%d/%y"))
        tmp = []
        for data in d[d.index(first):]:
            tmp.append(self.confirmed_case[data])
        return tmp


def main(args):
    n_cases = int(args["number"])
    interested = args["list"]
    interested = interested.split(",")


    if not os.path.isdir("./DataSet"):
        os.mkdir("./DataSet")

    confirmed_temp_path = "./DataSet/confirmed_tmp.csv"
    confirmed_final_path = "./DataSet/confirmed_time.csv"


    # Refresh Files.

    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
                                   "csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv",
                                   confirmed_temp_path
                                   if os.path.isfile(confirmed_final_path)
                                   else confirmed_final_path)
        if os.path.isfile(confirmed_temp_path):
            sha256_temp = hashlib.sha256(file_as_bytes(open(confirmed_temp_path, 'rb'))).hexdigest()
            sha256_time = hashlib.sha256(file_as_bytes(open(confirmed_final_path, 'rb'))).hexdigest()

            if sha256_temp != sha256_time:
                os.remove(confirmed_final_path)
                os.rename(confirmed_temp_path, confirmed_final_path)
                print("New File")
            else:
                os.remove(confirmed_temp_path)
    except urllib.request.URLError:
        print("URL Error")

    list_country = {}

    with open(confirmed_final_path, 'r') as file:

        list_dates = file.readline().strip('\n').split(',')[4:]

        for line in file:
            if line.startswith('#'):
                continue
            # Prepare Parsing
            line = line.replace(line[line.find('"'):line.rfind('"')+1], "")
            sp_line = line.strip('\n').split(',')

            # Parse details
            province = sp_line[0]
            country = sp_line[1]
            lat = float(sp_line[2])
            long = float(sp_line[3])

            confirmed = {}

            for i in range(0, len(list_dates)):
                confirmed[list_dates[i]] = int(sp_line[i+4])

            if country in list_country.keys():
                old_confirmed = list_country[country].confirmed_case
                new_confirmed = \
                    {k: old_confirmed.get(k, 0) + confirmed.get(k, 0) for k in set(old_confirmed) & set(confirmed)}
                list_country[country] = Country(country, new_confirmed)
            else:
                list_country[country] = Country(country, confirmed)

    for item in interested:
        if item not in list_country.keys():
            raise ValueError("Country " + item + " not found.")

    v = []

    ax = plt.axes()

    for paese in interested:
        tmp = list_country[paese].ordered_list_confirmed(n_cases)
        v += tmp
        plt.plot(range(0, len(tmp)), tmp, "--o", label=paese, axes=ax)

    if n_cases == 0:
        plt.xlabel("Days from January 22, 2020")
    else:
        plt.xlabel("Days from " + f"{n_cases:,}" + " cases event")

    ax.yaxis.set_major_formatter(tick.FuncFormatter(kmb_formatter))
    ax.set_yticks(np.linspace(min(v), max(v), num=10))

    plt.title("Confirmed from n. cases: " + str(n_cases))
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="COVID-19 Visualizer")
    parser.add_argument("-n", "--number", required=False, default=0, help="Number of cases as starting event")
    parser.add_argument("-l", "--list", required=True, help="List of countries under analysis")

    main(vars(parser.parse_args()))

