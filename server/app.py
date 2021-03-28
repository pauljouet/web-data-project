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


# endpoint to get stations
@app.route('/api/stations', methods=['GET'])
def stations():
    # functionGetStation returns the structured array of stations from triplestor
    stations = getStationsData()
    return jsonify(stations)


# endpoint to get museums
@app.route('/api/museums', methods=['GET'])
def museums():
    museums= getMuseumData()
    return jsonify(museums)

# endpoint to get monuments
@app.route('/api/monuments', methods=['GET'])
def monuments():
    monuments=getMonumentData()
    return jsonify(monuments)


@app.route('/api/getdata', methods=['GET'])
def getData():
    # functionGetStation returns the structured array of stations from triplestor
    filter=request.args.get('filter', 'stations')
    data={}
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