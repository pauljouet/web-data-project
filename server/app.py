# API flask to access the server with the client JS code
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from fuseki_managements.bikeStation import getStationsData
from fuseki_managements.monument import getMonumentData
from fuseki_managements.manage_fuseki import deleteDefaultGraph
# import functions to get stations
# import functions to get museums
# import functions to get monument


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
    museums= functionGetMuseums()
    return jsonify(museums)

# endpoint to get monuments
@app.route('/api/monuments', methods=['GET'])
def monuments():
    monuments=getMonumentData()
    return jsonify(monuments)


# endpoint to get monuments
@app.route('/api/deleteAll', methods=['GET'])
def monuments():
    rep=deleteDefaultGraph()
    return jsonify(rep)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)