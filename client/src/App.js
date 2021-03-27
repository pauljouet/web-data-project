import './App.css';

import React, { useEffect } from 'react';
import { useState } from 'react';
import ReactMapGL, { Marker, Popup } from 'react-map-gl';
import { Monument, Museum, BikeStation } from './components';
const data = require('./Data')





// TODO utiliser des buildings récupérés du dataset

const tqt = [{
  id: "123",
  type:"monument",
  name: "Super immeuble qui tue sa mère",
  lat: 48.850853542905114,
  lon: 2.343891862961394,
  city: "Paris",
  description: "Un immeuble ultra boosté qui tue sa mère"
}, {
  id: "1234",
  type:"Museum",
  name: "Centre Pompidou",
  lat: 48.8611698632859, 
  lon: 2.351691564900129,
  address: "Place George Pompidou",
  city: "Paris",
  description: "Centre d'art le plus iconique de la capitale",
},
{
  id: "12345",
  type:"BikeStation",
  name: "Super station",
  lat: 48.863358024171255, 
  lon: 2.335523642208444,
  city: "Paris",
  cap:30,
  avBikes: 13,
  avDocks:15,
}
]


// main componend

export default function App() {


  // detail for the map component
  const [viewport, setViewport] = useState({
    width: "100vw",
    height: "100vh",
    latitude: 48.856614,
    longitude: 2.3522219,
    zoom: 12
  });

  const [elements, setElements] =  useState([]);

  // promise.all runs the 3 fetching in parrallel to gain time
  useEffect( ()=>{
      Promise.all([data.fetchStation()])
        .then(result => setElements(result.flat()))
  }, []);

  
  //state to keep in memory the clicked elements and change when needed
  const [selectedElement, setSelectedElement] = useState(null)



  return (
    <div>
    <div className="App-header">
      <h1>Bike Touristic Tour</h1>
    </div>
    <div>
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
        mapStyle="mapbox://styles/mapbox/streets-v11"
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



