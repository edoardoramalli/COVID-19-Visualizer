# COVID-19-Visualizer
Visualizer of COVID-19 Cases. Compare the number of cases in different countries. You can also shift the starting point of visualization based on the first xx cases reported, to compare the spread of the virus.

## Start 

`python3 COVID-19.py [-n] -l Country1,Country2,...`

- `-n` number of reported cases from which the visualization start. If 0 visualize all history
- `-l` list of countries. Each country should be separeted by a comma, if more than one is present.

### Example 2

`python3 COVID-19.py  -l Italy,US,France,Germany`

This command generate the visualization for Italy, US, France, Germany from January 22, 2020.
![Image 1](https://github.com/edoardoramalli/COVID-19-Visualizer/blob/master/img/img.png)

### Example 2

`python3 COVID-19.py -n 500 -l Italy,US,France,Germany`

This command generate the visualization for Italy, US, France, Germany from when each of them has 500 reported cases.
So we perform a temporal shift to compare the speed of spread curve.
![Image 1](https://github.com/edoardoramalli/COVID-19-Visualizer/blob/master/img/img2.png)

### List of Countries
|Name|||||||
|:------------|:------------|:------------|:------------|:------------|:------------|:------------|
|Afghanistan	|Albania	|Algeria	|Andorra	|Angola	|Antigua and Barbuda	|Argentina	|Armenia	|
|Australia	|Austria	|Azerbaijan	|Bahrain	|Bangladesh	|Barbados	|Belarus	|Belgium	|
|Benin	|Bhutan	|Bolivia	|Bosnia and Herzegovina	|Brazil	|Brunei	|Bulgaria	|Burkina Faso	|
|Cabo Verde	|Cambodia	|Cameroon	|Canada	|Cape Verde	|Central African Republic	|Chad	|Chile	|
|China	|Colombia	|Congo (Brazzaville)	|Congo (Kinshasa)	|Costa Rica	|Cote d'Ivoire	|Croatia	|Cruise Ship	|
|Cuba	|Cyprus	|Czechia	|Denmark	|Djibouti	|Dominican Republic	|East Timor	|Ecuador	|
|Egypt	|El Salvador	|Equatorial Guinea	|Eritrea	|Estonia	|Eswatini	|Ethiopia	|Fiji	|
|Finland	|France	|Gabon	|Georgia	|Germany	|Ghana	|Greece	|Guatemala	|
|Guinea	|Guyana	|Haiti	|Holy See	|Honduras	|Hungary	|Iceland	|India	|
|Indonesia	|Iran	|Iraq	|Ireland	|Israel	|Italy	|Jamaica	|Japan	|
|Jordan	|Kazakhstan	|Kenya	|Kosovo	|Kuwait	|Kyrgyzstan	|Latvia	|Lebanon	|
|Liberia	|Liechtenstein	|Lithuania	|Luxembourg	|Madagascar	|Malaysia	|Maldives	|Malta	|
|Martinique	|Mauritania	|Mauritius	|Mexico	|Moldova	|Monaco	|Mongolia	|Montenegro	|
|Morocco	|Namibia	|Nepal	|Netherlands	|New Zealand	|Nicaragua	|Niger	|Nigeria	|
|North Macedonia	|Norway	|Oman	|Pakistan	|Panama	|Papua New Guinea	|Paraguay	|Peru	|
|Philippines	|Poland	|Portugal	|Qatar	|Romania	|Russia	|Rwanda	|Saint Lucia	|
|Saint Vincent and the Grenadines	|San Marino	|Saudi Arabia	|Senegal	|Serbia	|Seychelles	|Singapore	|Slovakia	|
|Slovenia	|Somalia	|South Africa	|Spain	|Sri Lanka	|Sudan	|Suriname	|Sweden	|
|Switzerland	|Taiwan*	|Tanzania	|Thailand	|Togo	|Trinidad and Tobago	|Tunisia	|Turkey	|
|US	|Uganda	|Ukraine	|United Arab Emirates	|United Kingdom	|Uruguay	|Uzbekistan	|Venezuela	|
|Vietnam	|Zambia	|Zimbabwe|||||||

### Reference
The visualizer uses the datat of https://github.com/CSSEGISandData/COVID-19
