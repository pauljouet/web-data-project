# file to get / insert bikeStation in the knwoledge base
# use the manage.py functions
# must use the biek station APIs to get real time data


from manage-fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile
from get_data import mapStationStatus

storeFile = "server/fuseki-managements/datasets/station-info.jsonld"

queryfile="server/fuseki-managements/queries/query-bike.txt"

def updateStationsData():
    deleteDefaultGraph()
    insertOntology()
    # fetch station data from velib API and put it in a json ld
    mapSationStatus(storeFile)
    # store the jsonfile into the triple store
    insertEntries(storeFile)



def getStationsData():
    data=queryFromFile(queryFile)
    return data








