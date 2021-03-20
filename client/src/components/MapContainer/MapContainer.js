import './MapContainer.css';

import * as React from 'react';
import { useState } from 'react';
import ReactMapGL, { Marker, Popup } from 'react-map-gl';
require('dotenv').config()



function MapContainer({ historicalBuilding }) {
    const [viewport, setViewport] = useState({
        width: "100vw",
        height: "100vh",
        latitude: 48.856614,
        longitude: 2.3522219,
        zoom: 10
    });

    const [selectedHistoricalMonument, setSelectedHistoricalMonument] = useState(null)

    return (
        <div>
            <ReactMapGL
                {...viewport}
                mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
                mapStyle="mapbox://styles/mapbox/streets-v11"
                onViewportChange={nextViewport => setViewport(nextViewport)}
            >
                
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
                

                {selectedHistoricalMonument ? (
                    <Popup 
                     latitude = {selectedHistoricalMonument.latitude}
                     longitude= {selectedHistoricalMonument.longitude}>
                        <div>
                            {selectedHistoricalMonument.description}
                        </div>
                    </Popup>
                ): null}

            </ReactMapGL>

        </div>

    );
}

export default MapContainer;