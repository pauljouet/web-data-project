import * as React from 'react';
import { useState } from 'react';
import ReactMapGL from 'react-map-gl';
require('dotenv').config()


const REACT_APP_MAPBOX_TOKEN="pk.eyJ1IjoiZmxvcmVudGRyaWxoaG9uIiwiYSI6ImNrbWh0YnZoZjBhbTkzMXMxZzBmNzRpODYifQ.pKLn68tATvgzJyVDjGC1dQ"

function MapContainer() {
  const [viewport, setViewport] = useState({
    width: 400,
    height: 400,
    latitude: 48.856614,
    longitude:2.3522219,
    zoom: 8
  });

  return (
    <ReactMapGL
      {...viewport}
      mapboxApiAccessToken={REACT_APP_MAPBOX_TOKEN}
      onViewportChange={nextViewport => setViewport(nextViewport)}
    />
  );
}

export default MapContainer;