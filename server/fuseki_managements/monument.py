# file to get / insert monument in the knwoledge base
# use the manage.py functions
from fuseki_managements.manage_fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile
from fuseki_managements.get_data import mapMonument


queryfile='get-monuments.txt'
storefile=os.path.join(os.path.dirname(__file__), "./datasets/monuments.jsonld")

def insertMonuments():
    mapMonument(storefile)
    insertEntries(storefile)


# format data sent back by the fuseki server
def formatData(data):
    for key in data.keys():
        data[key]=data[key]["value"]
    data["lat"]=float(data["lat"])
    data["lon"]=float(data["lon"])
    data["type"]="monument"
    return data

def getMonumentData():
    monuments=queryFromFile(queryfile)
    for monument in monuments:
        monument=formatData(monument)
    return monuments


