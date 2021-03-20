import './App.css';

import React from 'react';
import { useState } from 'react';
import ReactMapGL, { Marker, Popup } from 'react-map-gl';


import {HistoricalBuilding} from './components';


// TODO utiliser des buildings récupérés du dataset

const historicalBuildings = [{
  _id: "123",
  name: "Super immeuble qui tue sa mère",
  latitude: 48.850853542905114,
  longitude: 2.343891862961394,
  address: "12 Boulevard du Général de Gaule",
  city: "Paris",
  description: "Un immeuble ultra boosté qui tue sa mère"
}]


// main componend

export default function App() {


  // detail for the map component
  const [viewport, setViewport] = useState({
    width: "100vw",
    height: "100vh",
    latitude: 48.856614,
    longitude: 2.3522219,
    zoom: 10
  });

  //state to keep in memory the clicked elements and change when needed
  const [selectedHistoricalMonument, setSelectedHistoricalMonument] = useState(null)

  return (
    <div>
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
        mapStyle="mapbox://styles/mapbox/streets-v11"
        onViewportChange={nextViewport => setViewport(nextViewport)}
      >
        {historicalBuildings.map(historicalBuilding => (

          <Marker
            key={historicalBuilding._id}
            latitude={historicalBuilding.latitude}
            longitude={historicalBuilding.longitude}
          >
            <button
              className="marker-btn"
              onClick={event => {
                event.preventDefault();
                setSelectedHistoricalMonument(historicalBuilding)
              }}
            >
              <img src="/monument.svg" alt="Monument Icon" />

            </button>
          </Marker>

        ))}
        {selectedHistoricalMonument ? (
          <Popup
            latitude={selectedHistoricalMonument.latitude}
            longitude={selectedHistoricalMonument.longitude}
            onClose={()=> {
              setSelectedHistoricalMonument(null);
            }}
            >
            <div>
            <HistoricalBuilding
              building={selectedHistoricalMonument}
            />
            </div>
          </Popup>
        ) : null}

      </ReactMapGL>

    </div>
  );
}



