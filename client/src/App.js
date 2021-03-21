import './App.css';

import React from 'react';
import { useState } from 'react';
import ReactMapGL, { Marker, Popup } from 'react-map-gl';


import { HistoricalBuilding, Museum, BikeStation } from './components';


// TODO utiliser des buildings récupérés du dataset

const elements = [{
  _id: "123",
  type:"Historical monument",
  name: "Super immeuble qui tue sa mère",
  latitude: 48.850853542905114,
  longitude: 2.343891862961394,
  address: "12 Boulevard du Général de Gaule",
  city: "Paris",
  description: "Un immeuble ultra boosté qui tue sa mère"
}, {
  _id: "1234",
  type:"Museum",
  name: "Centre Pompidou",
  latitude: 48.8611698632859, 
  longitude: 2.351691564900129,
  address: "Place George Pompidou",
  city: "Paris",
  description: "Centre d'art le plus iconique de la capitale",
  openingTime : "9h00-17h30"
},
{
  _id: "12345",
  type:"BikeStation",
  name: "Super station",
  latitude: 48.863358024171255, 
  longitude: 2.335523642208444,
  address: "Avenue de l'Opéra",
  city: "Paris",
  availableBikes: 13,
  freeSlots:15,
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
            key={element._id}
            latitude={element.latitude}
            longitude={element.longitude}
          >
            <button
              className="marker-btn"
              onClick={event => {
                event.preventDefault();
                setSelectedElement(element)
              }}
            >
              {element.type ==="Historical monument" ?
                <img src="/monument.svg" alt="Monument Icon" />
                 : (element.type ==="Museum" ?
                 <img src="/museum.svg" alt="Museum Icon" />
                  : <img src="/bike.svg" alt="Monument Icon" />)
              }
              

            </button>
          </Marker>

        ))}
        {selectedElement ? (
          <Popup
            latitude={selectedElement.latitude}
            longitude={selectedElement.longitude}
            onClose={() => {
              setSelectedElement(null);
            }}
          >
            <div>
              {selectedElement.type ==="Historical monument" ?
                <HistoricalBuilding
                  building={selectedElement}
                /> : (selectedElement.type ==="Museum" ?
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



