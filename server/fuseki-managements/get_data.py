#! usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from rdflib import Graph, Namespace, BNode

ns = Namespace("http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#")
url_velib1 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
url_velib2 = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
context = """
"@context": {
 "@vocab": "http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#",
 "station_id" : "hasID",
 "lat": "hasLatitude",
 "lon": "hasLongitude",
 "capacity": "hasCapacity",
 "name": "hasName",
  "lastUpdatedOther": null,
  "ttl": null,
 "stationCode": null},
 """

def mapStationStatus():
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

    for i in range(10):
        print(stations[i])

    data = {"@context": {"@vocab": "http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#"}, "stations": stations}

    with open('test-station-format.json', 'w') as outfile:
        json.dump(data, outfile)

    return stations



mapStationStatus()
createTriples()