# web-data-project

Web application project that regroups in the same interface :

- bike-stations
- museums
- historical monuments

The goal is to create a web app that can be used for green touristic tour in Paris. The users sould be able to know where to rent a bike next to them, and what are the museum and historic buildings at proximity.


Used sources :

- bike api (real time) : http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&rows=1500
                         https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole
                         
- historical monument dataset : https://www.data.gouv.fr/fr/datasets/monuments-historiques-liste-des-immeubles-proteges-au-titre-des-monuments-historiques/
- museums dataset : https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/

The goal is to get the information and to store it in knowledge base in RDF, to then call it and use it in the web application.

So the programm is divided in several parts, each of one answer a specific part of the application.

- Analyse the data and design the ontology with Protege
- Store the data in the ontology and find a way to query it
- Build a web app with react and query the data stored to render it

