# API flask to access the server with the client JS code
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from fuseki_managements.bikeStation import getStationsData
from fuseki_managements.monument import getMonumentData
from fuseki_managements.museum import getMuseumData
from fuseki_managements.manage_fuseki import deleteDefaultGraph



app=Flask(__name__)
CORS(app)


# first endpoint
@app.route('/', methods=['GET'])
def home():
    res= {'ack': True}
    return res


# endpoint to get all type of data
@app.route('/api/getdata', methods=['GET'])
def getData():
    # get the filter precised in RESTful URL, default = stations
    filter=request.args.get('filter', 'stations')
    data={}
    # get the corresponding ressources from triplestore
    if filter == 'stations':
        data=getStationsData()
    elif filter == 'museums':
        data=getMuseumData()
    elif filter == 'monuments':
        data=getMonumentData()
    else :
        data={'error': 'could not find ressource : {}'.format(filter)}
    return jsonify(data)

# must be ran from the server (current) folder
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)