# web-data-project

Web application project that regroups in the same interface :

- les stations des vélos
- les musées
- les bâtiments historiques dans Paris


Sources utilisées :

- vélos api (temps réel) : http://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&rows=1500
- monuments historiques dataset : https://www.data.gouv.fr/fr/datasets/monuments-historiques-liste-des-immeubles-proteges-au-titre-des-monuments-historiques/
- musées dataset : https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/

The goal is to get the information and to store it in knowledge base in RDF, to then call it and use it in the web application.

So the programm is divided in several parts, each of one answer a specific part of the application.

- Analyse the data and design the ontology with Protege
- Store the data in the ontology and find a way to query it
- Build a web app with react and query the data stored to render it

