#! usr/bin/env python3
# -*- coding: utf-8 -*-

from rdflib import Graph, URIRef
import rdflib.plugin
import requests
from rdflib.plugins.stores import sparqlstore
import os

SERVER_URL = "http://localhost:3030"
DATASET_URL = SERVER_URL + "/webdata-project-kb"
SPARQL_ENDPOINT = DATASET_URL + "/sparql"
QUERY_ENDPOINT = DATASET_URL + "/query"
SPARQL_UPDATE = DATASET_URL + "/update"
GRAPH_STORE = DATASET_URL + "/data"
HEADERS_QUERY = {'Content-type': 'application/sparql-query'}
HEADERS_UPDATE = {'Content-type': 'application/sparql-update'}

queries_folder = os.path.join(os.path.dirname(__file__), "./queries/")
station_json = os.path.join(os.path.dirname(__file__), "./datasets/stations.jsonld")
monument_json = os.path.join(os.path.dirname(__file__), "./datasets/monuments.jsonld")
loc_ontology = os.path.join(os.path.dirname(__file__), "../ontology/project-ontology.ttl")

# query to delete all the rows in the knowledge base
def deleteQuery():
    """
        Returns a string with a query deleting all triples in the KB
    """
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

def insertQuery(s, p, o):
    """
        Inserts a triple into the KB
        Input: s -> subject p -> predicate o -> object
    """

    return """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX ns: <http://http://www.semanticweb.org/pauljouet/ontologies/2021/2/web-data-project#>
        INSERT DATA
        {
            """+ s + ' ' + p + ' ' + o + """ .
        }
    """

def queryFromFile(filename):
    """
        Asks the server (Fuseki triplestore) using a .txt file containing a SPARQL query
        Input: query file path
    """
    with open(os.path.join(os.path.dirname(__file__), "./queries/") + filename, 'r') as query:
        queryString = "".join(query.readlines())
    print(queryString)
    
    rep = requests.post(DATASET_URL, data=queryString, headers=HEADERS_QUERY)
    if rep.status_code != 200:
        rep.raise_for_status()
    data = rep.json()
    return data["results"]["bindings"]



def deleteDefaultGraph():
    """
        Deletes all triples in the default graph
    """
    rep = requests.post(DATASET_URL, data=deleteQuery(), headers=HEADERS_UPDATE)
    if rep.status_code != 204:
        rep.raise_for_status()

def insertEntries(filename):
    """
    Adds entries from a JSON-LD file to the triple store in the default graph
    Input: the path to the JSON-LD file
    """
    data = open(filename).read()
    headers = {'Content-Type': 'application/ld+json'}
    r = requests.post(GRAPH_STORE + '?default', data=data, headers=headers)
    if r.status_code != 204:
        r.raise_for_status()
    else:
        print("Status response",r)

def insertOntology():
    """
        Inserts the ontology into the default graph in Fuseki
    """
    data = open(loc_ontology).read()
    headers = {'Content-Type': 'text/turtle'}
    r = requests.post(GRAPH_STORE + '?default', data=data, headers=headers)
    if r.status_code != 204:
        r.raise_for_status()
    else:
        print("Status response",r)

def main():
    #deleteDefaultGraph()
    #insertOntology()
    #insertEntries(monument_json)
    #insertEntries(station_json)
    #queryFromFile(queries_folder + "get-graph-names.txt")
    monuments= queryFromFile("get-stations.txt")
    for i in range(10):
        print(monuments[i])
        print(monuments[i]['lat']['value'])
    

if __name__ == "__main__":
    insertEntries(station_json)
    # main()