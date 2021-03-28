#! usr/bin/env python3
# -*- coding: utf-8 -*-

from manage_fuseki import insertEntries, insertOntology
import os

station_json = os.path.join(os.path.dirname(__file__), "./datasets/stations.jsonld")
monument_json = os.path.join(os.path.dirname(__file__), "./datasets/monuments.jsonld")
musee_json = os.path.join(os.path.dirname(__file__), "./datasets/musees.jsonld")

if __name__ == "__main__":
    insertOntology()
    insertEntries(monument_json)
    insertEntries(musee_json)
    insertEntries(station_json)