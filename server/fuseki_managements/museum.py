# file to get / insert museum in the knwoledge base
# use the manage.py functions
from fuseki_managements.manage_fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile



def formatData(data):
    for key in data.keys():
        data[key]=data[key]["value"]
    data["lat"]=float(data["lat"])
    data["lon"]=float(data["lon"])
    data["type"]="museum"
    return data


def getMuseumData():
    # TODO update station data before query
    stations=queryFromFile('get-museums.txt')
    for station in stations:
        station=formatData(station)
    return stations