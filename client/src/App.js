import './App.css';

import React, { useEffect } from 'react';
import { useState } from 'react';
import ReactMapGL, { Marker, Popup } from 'react-map-gl';
import { Monument, Museum, BikeStation } from './components';
const data = require('./Data')

// main component

export default function App() {

  const [elements, setElements] =  useState([]);
  //state to keep in memory the clicked elements and change when needed
  const [selectedElement, setSelectedElement] = useState(null);
  const [loading, setLoading] = useState(true);
  // detail for the map component
  const [viewport, setViewport] = useState({
    width: "100vw",
    height: "100vh",
    latitude: 48.856614,
    longitude: 2.3522219,
    zoom: 12
  });

  

  // promise.all runs the 3 fetching in parrallel to gain time
  useEffect( ()=>{
    if(loading) {
      console.log('loading');
      Promise.all([data.fetchStation()])
        .then(result => setElements(result.flat()))
    }
  }, [loading]);

  useEffect(() => {
    setLoading(false);
  }, [elements]);


  return (
    <div>
    <div className="App-header">
      <h1>Bike Touristic Tour</h1>
    </div>
    <div>
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
        mapStyle="mapbox://styles/mapbox/outdoors-v11"
        onViewportChange={nextViewport => setViewport(nextViewport)}
      >
        {elements.map(element => (

          <Marker
            key={element.id}
            latitude={element.lat}
            longitude={element.lon}
          >
            <button
              className="marker-btn"
              onClick={event => {
                event.preventDefault();
                setSelectedElement(element)
              }}
            >
              {element.type ==="monument" ?
                <img src="/monument.svg" alt="Monument Icon" />
                 : (element.type ==="museum" ?
                 <img src="/museum.svg" alt="Museum Icon" />
                  : <img src="/bike.svg" alt="Bike Icon" />)
              }
              

            </button>
          </Marker>

        ))}
        {selectedElement ? (
          <Popup
            latitude={selectedElement.lat}
            longitude={selectedElement.lon}
            onClose={() => {
              setSelectedElement(null);
            }}
          >
            <div>
              {selectedElement.type ==="monument" ?
                <Monument
                  monument={selectedElement}
                /> : (selectedElement.type ==="museum" ?
                  <Museum museum={selectedElement} />
                  : <BikeStation station={selectedElement} />)
              }

            </div>
          </Popup>
        ) : null}

      </ReactMapGL>

    </div>
  </div>
  );
}



