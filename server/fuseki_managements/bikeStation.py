# file to get / insert bikeStation in the knwoledge base
# use the manage.py functions
# must use the biek station APIs to get real time data


from fuseki_managements.manage_fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile
from fuseki_managements.get_data import mapStationStatus

storeFile1 = "./datasets/station-info.jsonld"

queryfile="./queries/query-bike.txt"


# delete all bikeStations and replace them with new real time information from the API
def updateStationsData():


    deleteDefaultGraph()
    insertOntology()
    # fetch station data from 1st velib API and put it in a json ld
    mapStationStatus(storeFile1)

    #fetch station data from 2nd velib API and put it in a json ld
    # mapStationFunction 

    # store the jsonfile into the triple store
    insertEntries(storeFile1)





# return all stations from the triplestore
def getStationsData():
    #data=queryFromFile(queryFile)
    #print(data)
    bikeStation={"name":"Boucicaut", "capacity": 28, "availableSlots":12, "description": 'test'}
    return bikeStation




if __name__ == "__main__":
    updateStationsData()








