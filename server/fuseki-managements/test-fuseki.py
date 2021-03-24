#! usr/bin/env python3
# -*- coding: utf-8 -*-

from rdflib import Graph, URIRef
from rdflib.plugin import *
import requests
import os
from rdflib.plugins.stores import sparqlstore

SERVER_URL = "http://localhost:3030"
DATASET_URL = SERVER_URL + "/webdata-project-kb"
SPARQL_ENDPOINT = DATASET_URL + "/sparql"
QUERY_ENDPOINT = DATASET_URL + "/query"
SPARQL_UPDATE = DATASET_URL + "/update"
GRAPH_STORE = DATASET_URL + "/data"
HEADERS_QUERY = {'Content-type': 'application/sparql-query'}
HEADERS_UPDATE = {'Content-type': 'application/sparql-update'}

filename= "paris-museum-query.txt"
stations_file1 = "test-station-format.jsonld"

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

def deleteFromGraphQuery(graph_url):
    return """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
        DELETE
        {
            ?s ?p ?o
        }
        WHERE
        {
            GRAPH <"""+graph_url+""">
            {
                ?s ?p ?o
            }
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

def deleteGraph(graph_url):
    rep = requests.post(DATASET_URL, data=deleteFromGraphQuery(graph_url), headers=HEADERS_UPDATE)
    if rep.status_code != 204:
        rep.raise_for_status()

def updateGraph(filename):
    """
    store = sparqlstore.SPARQLUpdateStore()
    store.open((QUERY_ENDPOINT, SPARQL_UPDATE))

    g = Graph(identifier = URIRef(DATASET_URL))
    g.parse(location=filename, format='json-ld')
    print(g)

    store.add_graph(g)
    """
    data = open(stations_file1).read()
    headers = {'Content-Type': 'application/ld+json'}
    r = requests.post(GRAPH_STORE + '?default', data=data, headers=headers)
    if r.status_code != 204:
        r.raise_for_status()

def main():
    #updateGraph(stations_file1)
    deleteGraph(GRAPH_STORE + "?bikestation-test1")

if __name__ == "__main__":
    main()