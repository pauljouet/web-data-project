#! usr/bin/env python3
# -*- coding: utf-8 -*-

# file to get / insert bikeStation in the knwoledge base
# use the manage.py functions
# must use the biek station APIs to get real time data


from manage_fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile
from get_data import mapStationStatus
import os
import requests

HEADERS_UPDATE = {'Content-type': 'application/sparql-update'}
DATASET_URL = "http://localhost:3030/webdata-project-kb"

storeFile1 = os.path.join(os.path.dirname(__file__), "./datasets/station-info.jsonld")
queryfile="query-bike.txt"


# delete all bikeStations and replace them with new real time information from the API
def updateStationsData():
    rep = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json")
    data = rep.json()
    stations = data["data"]["stations"]

    for station in stations:
        id = station['station_id']
        bikes = station['num_bikes_available']
        bikes = '"' + str(bikes) + '"^^xsd:int'
        docks= station['num_docks_available']
        docks = '"' + str(docks) + '"^^xsd:int'
        updateQueryString = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

            DELETE
            {
                ?s ns:hasAvailableDocks ?o1 .
                ?s ns:hasAvailableBikes ?o2 .
            }
            WHERE
            {
                ?s ns:hasID """ + str(id) + """ .
                ?s ns:hasAvailableDocks ?o1 .
                ?s ns:hasAvailableBikes ?o2 .
            } ;

            INSERT
            {
                ?s ns:hasAvailableDocks """ + docks + """ .
                ?s ns:hasAvailableBikes """ + bikes + """ .
            }
            WHERE
            {
                ?s ns:hasID """ + str(id) + """ .
            }
        """
        #print(updateQueryString)
        rep = requests.post(DATASET_URL, data=updateQueryString, headers=HEADERS_UPDATE)
        if rep.status_code != 204:
            rep.raise_for_status()

def updateStationsDatav2():
    deleteStations = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
        DELETE
        {
            ?s ns:hasName ?name .
            ?s ns:hasID ?id .
            ?s ns:hasLatitude ?lat .
            ?s ns:hasLongitude ?lon .
            ?s ns:hasCapacity ?capa .
            ?s ns:hasAvailableBikes ?avbikes .
            ?s ns:hasAvailableDocks ?avdocks .
        }
        WHERE
        {
            ?s ns:hasName ?name .
            ?s ns:hasID ?id .
            ?s ns:hasLatitude ?lat .
            ?s ns:hasLongitude ?lon .
            ?s ns:hasCapacity ?capa .
            ?s ns:hasAvailableBikes ?avbikes .
            ?s ns:hasAvailableDocks ?avdocks .
        }
    """
    #A COMPLETEEER

    for station in stations:
        pass


if __name__ == "__main__":
    #updateStationsData()
    # so this function works, but it is slower than removing all of the stations' data
    pass








