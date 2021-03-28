import requests
from dotenv import load_dotenv
import os
from pathlib import Path  # Python 3.6+ only
env_path = 'fuseki_managements/.env'

load_dotenv(dotenv_path=env_path)
MAPS_API_KEY=os.getenv("MAPS_API_KEY")

# Convert string to location
def getCoordinates(location):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'key':MAPS_API_KEY , 'address': location}
    #print("key:", MAPS_API_KEY)
    response = requests.get(url, params=params)
    # If not sucess raise error
    if response.status_code != 200:
        print("error in status")
        response.raise_for_status()
        return (None, None)
    results = response.json()['results']
    # return results if we find one
    if len(results):
        location = results[0]['geometry']['location']
        return (location['lat'], location['lng'])
    else:
        return (None, None)


if __name__=="__main__":
    coordinates=getCoordinates("63 boulevard de Brou Bourg-En-Bresse")
    print(coordinates)