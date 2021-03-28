# web-data-project
## Overview

Web application project that regroups in the same interface :

- bike-stations 🚲
- museums 🖼
- historical monuments 🏛

The goal is to create a web app that can be used for green touristic tour in Paris. The users sould be able to know where to rent a bike next to them, and what are the museum and historic buildings nearby. The application should provide useful information about the places to visit, and make itinerary recommandations to the user based on the availability of the bikes nearby and the possibility of leaving the bike near the monument/museum.



### Demo

Here is a little demo of our platform (in local use)


![](./figures/demo.gif)



### How to install



### How to run




## Explanations

### How to collect information

The information we need from the opensource databases are:
•	the geolocation and adresses of the museums, historic monuments and bike stations
•	names and descriptions for the places to visit
•	number of bikes and room available for the stations
•	identifiers

Our sources:
•	bike api (real time) : https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole
for station_id, hasLatitude, hasLongitude, hasName and hasCapacity : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json for station_id, hasAvailableBikes : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json
•	historical monument dataset : https://www.data.gouv.fr/fr/datasets/monuments-historiques-liste-des-immeubles-proteges-au-titre-des-monuments-historiques/
•	museums dataset : https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/
Once the data collected from these sources the first thing to do is to pre-process it in order to have only the needed informations. Once it’s done we had to format it into JSON LD to push it into the knowledge database of fuseki and for the flask application ; the use of these tools will be explaied afterwards. 
xThe informations about the bike stations are updated every time we want to check them.
We chose to focus our application on Paris, to be able to do so we used queries on our collected and pre-precessed data.


