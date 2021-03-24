#! usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

ns = "http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#"
url_velib1 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
url_velib2 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
station_json1 = "server/fuseki-managements/datasets/station-info.jsonld"

def mapStationStatus(storeFile):
    """
        Creates a JSON-LD file in the datasets folder with the latest infos on the velib stations
    """
    rep = requests.get(url_velib1)
    data = rep.json()
    stations = data["data"]["stations"]
    for station in stations:
        station['hasID'] = station.pop('station_id')
        station['hasName'] = station.pop('name')
        station['hasLatitude'] = station.pop('lat')
        station['hasLongitude'] = station.pop('lon')
        station['hasCapacity'] = station.pop('capacity')
        station.pop('stationCode', None)
        station.pop('rental_methods', None)

    #for i in range(10):
    #    print(stations[i])

    data = {"@context": {"@vocab": ns}, "stations": stations}

    with open(storeFile, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    mapStationStatus(station_json1)