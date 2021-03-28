# web-data-project
## Overview

Web application project that regroups in the same interface :

- bike-stations
- museums
- historical monuments

The goal is to create a web app that can be used for green touristic tour in Paris. The users sould be able to know where to rent a bike next to them, and what are the museum and historic buildings nearby. The application should provide useful information about the places to visit, and make itinerary recommandations to the user based on the availability of the bikes nearby and the possibility of leaving the bike near the monument/museum.

The information we need from the databases are:

- the geolocation and adresses of the museums, historic monuments and bike stations
- names and descriptions for the places to visit
- number of bikes and room available for the stations
- identifiers

**Our sources:**

- bike api (real time) : https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole  
      for station_id, hasLatitude, hasLongitude, hasName and hasCapacity : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json             for station_id, hasAvailableBikes : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json
- historical monument dataset : https://www.data.gouv.fr/fr/datasets/monuments-historiques-liste-des-immeubles-proteges-au-titre-des-monuments-historiques/
- museums dataset : https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/

The goal is to get the information and to store it in knowledge base in RDF, to then call it and use it in the web application.

So the programm is divided in several parts, each of one answer a specific part of the application.

- Analyse the data from our sources and design the ontology accordingly (with Protege)
- Import the data, format it to fit in the ontology and query it (should be in real time, because of the changing bike availability)
- Display the information through a friendly user interface


### Demo

Here is a little demo of our platform (in local use)


![](./figures/demo.gif)