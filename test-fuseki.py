#! usr/bin/env python3
# -*- coding: utf-8 -*-

import rdflib
import requests

SERVER_URL = "http://localhost:3030"
DATASET_URL = SERVER_URL + "/webdata-project-kb"
SPARQL_ENDPOINT = DATASET_URL + "/sparql"
SPARQL_UPDATE = DATASET_URL + "/update"
GRAPH_STORE = DATASET_URL + "/data"
HEADERS_QUERY = {'Content-type': 'application/sparql-query'}
HEADERS_UPDATE = {'Content-type': 'application/sparql-update'}

filename= "paris-museum-query.txt"

def deleteQuery():
    return """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
        DELETE
        {
            ?s ?p ?o
        }
        WHERE
        {
            ?s ?p ?o
        }
    """

def insertQuery():
    return """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
        INSERT DATA
        {
            ns:id1234 rdf:type ns:Museum .
        }
    """

def queryFromFile(filename):
    with open(filename, 'r') as query:
        queryString = "".join(query.readlines())
    print(queryString)
    
    rep = requests.post(DATASET_URL, data=queryString, headers=HEADERS_QUERY)
    if rep.status_code != 200:
        rep.raise_for_status()
    data = rep.json()
    for triple in data["results"]["bindings"]:
        print(triple)

def deleteDefaultGraph():
    rep = requests.post(DATASET_URL, data=deleteQuery(), headers=HEADERS_UPDATE)
    if rep.status_code != 204:
        rep.raise_for_status()

def main():
    queryFromFile(filename)

if __name__ == "__main__":
    main()