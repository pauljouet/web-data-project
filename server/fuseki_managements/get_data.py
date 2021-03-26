#! usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import os

ns = "http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#"
url_velib1 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
url_velib2 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
url_monuments = "https://www.data.gouv.fr/fr/datasets/r/0dca8af6-fb5e-42d8-970f-2b369fe7e421"
station_json = os.path.join(os.path.dirname(__file__), "./datasets/stations.jsonld")
monument_json = os.path.join(os.path.dirname(__file__), "./datasets/monuments.jsonld")

def mapStation(storeFile):
    """
        Creates a JSON-LD file in the datasets folder with the latest infos on the velib stations
    """
    rep = requests.get(url_velib1)
    rep2 = requests.get(url_velib2)
    data = rep.json()
    data2 = rep2.json()
    stations = data["data"]["stations"]
    stations2 = data2["data"]["stations"]

    for station in stations:
        station['hasID'] = station.pop('station_id')
        station['hasName'] = station.pop('name')
        station['hasLatitude'] = station.pop('lat')
        station['hasLongitude'] = station.pop('lon')
        station['hasCapacity'] = station.pop('capacity')
        station.pop('stationCode', None)
        station.pop('rental_methods', None)
        
    for station in stations2:
        station['hasID'] = station.pop('station_id', None)
        station['hasAvailableBikes'] = station.pop('num_bikes_available', None)
        station['hasAvailableDocks']= station.pop('num_docks_available', None)
        station.pop('stationCode', None)
        station.pop('numBikesAvailable', None)
        station.pop('num_bikes_available_types', None)
        station.pop('numDocksAvailable', None)
        station.pop('is_installed', None)
        station.pop('is_returning', None)
        station.pop('is_renting', None)
        station.pop('last_reported', None)

    stations_merged = []
    for i in range(len(stations)):
        if stations[i]['hasID'] == stations2[i]['hasID']:
            stations_merged.append({**stations[i], **stations2[i]})

    print(len(stations), len(stations_merged))

    for i in range(10):
        print(stations_merged[i])

    data = {"@context": {"@vocab": ns}, "stations": stations_merged}

    with open(storeFile, 'w') as outfile:
        json.dump(data, outfile)

def mapMonument(storeFile):
    """
        Creates a JSON-LD file in the datasets folder with the infos on the historical monuments
    """
    #with open('path/to/dataset') as json_file:
        #data = json.load(json_file)

    rep = requests.get(url_monuments)
    monuments = rep.json()

    good_monuments=[]
    for monument in monuments:
        dic={}  
        try:
            lat = monument["fields"]["coordonnees_ban"][0]
            lon = monument["fields"]["coordonnees_ban"][1]
            dic['hasLatitude'] = lat
            dic['hasLongitude'] = lon
            dic['hasName'] = monument["fields"]["tico"]
            dic['hasID'] = monument["fields"]["ref"]
            dic['hasDescription'] = monument["fields"]["ppro"]
            dic['hasCity'] = monument["fields"]["commune"]
            good_monuments.append(dic)
        except KeyError:
            a=0

    #for i in range(10):
    #    print(good_monuments[i])

    data = {"@context": {"@vocab": ns}, "monuments": good_monuments}

    with open(storeFile, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    #mapMonument(monument_json)
    #mapStation(station_json)
    