# Bike Touristic Tour

(Web Datamining & Semantics final project)


Made by [Florent Drilhon](https://github.com/florentdrilhon), [Paul Jouët](https://github.com/pauljouet) and [Aladin Homsy](https://github.com/aladeen57)


-  [Overview](#-overview)
- 👀 [Project Demo](#-demo)
- 📝 [Installation Guide](#-how-to-install)
- 🛠 [Project construction](#-explanations)



## Overview

Web application project that regroups in the same interface :

- bike-stations 🚲
- museums 🖼
- historical monuments 🏛

The goal is to create a web app that can be used for green touristic tour in Paris. The users sould be able to know where to rent a bike next to them, and what are the museum and historic buildings nearby. The application should provide useful information about the places to visit, and make itinerary recommandations to the user based on the availability of the bikes nearby and the possibility of leaving the bike near the monument/museum.

We chose to focus our application on Paris, to be able to do so we used queries on our collected and pre-precessed data.


### Demo

Here is a little demo of our platform (in local use)


![](./figures/demo.gif)



### How to install



### How to run




## Explanations

### How to collect information

The information we need from the opensource databases are:

- the geolocation and adresses of the museums, historic monuments and bike stations
- names and descriptions for the places to visit
- number of bikes and room available for the stations
- identifiers

Our sources:

- bike api (real time) : https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole
for station_id, hasLatitude, hasLongitude, hasName and hasCapacity : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json for station_id, hasAvailableBikes : https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json
- historical monument dataset : https://www.data.gouv.fr/fr/datasets/monuments-historiques-liste-des-immeubles-proteges-au-titre-des-monuments-historiques/
- museums dataset : https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/


Once the data collected from these sources the first thing to do is to pre-process it in order to have only the needed informations. To do so the file server/fuseki_managements/get_data.py use python to create a mapping from the data collected and store them into JSON LD files by adding our onlogy as context.

For the ontology, we created from scratch our own onlogy with protégé, here is a little overview : 

![](./figures/owl-viz-onto.PNG)

Once it’s done we had to format it into JSON LD to push it into the knowledge database of fuseki.


### Triplestore management


Once the data is inserted into the triplestore (fuseki), we had to define differents protocol to manage the data in the knowledge base. The file server/fuseki_managements/manage_fuseki.py connect to the triplestore and gather all useful functions to insert a JSON file or to make a query from a text file.

The functions defined in this file are used first to insert the JSON files into the database from the populate-db.py, and then to get the data of different types of ressources. To differentiate each type, we created respectively the files museum.py monument.py and bikeStation.py in folder server/fuseki_managements/ to differentiate the functions related to each ressource.

As the bikeStations are realtime data, we created an additionnal function for this ressource to update the wanted data before displaying it.

The functions defined for each ressource are then gathered in the server/app.py file which is a REST-based API to communicate with the client.

### Display the content

To display the content we chose to build a react APP in order to integrate a map to render the different GPS values. 

As introduced before, to get the data from the triplestore, the client will call the flask API that must be running (locally) during the process.

API url : http://localhost/api/getdata?filter=stations

where 'filter' can be replaced by 'monuments' or 'museums'.

To render the contents according to the right ressource, we defined custom react components in client/src/components where we precised how to render the elements, and we also included in the JSX (HTML) code the properties from the ontology we defined earlier.

The components are then called by the client/src/App.js file to integrate them according to their localisations in the map.





