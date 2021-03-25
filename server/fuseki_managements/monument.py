# file to get / insert monument in the knwoledge base
# use the manage.py functions
from fuseki_managements.manage_fuseki import deleteDefaultGraph, insertOntology, insertEntries, queryFromFile, formatData


queryfile='get-monuments.txt'

def getMonumentData():
    monuments=queryFromFile(queryfile)
    for monument in monuments:
        monument=formatData(monument)
    return monuments


