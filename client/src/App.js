import './App.css';

import {HistoricalBuilding, MapContainer} from './components'
import React, {Component} from 'react';



require('dotenv').config();




const historicalBuildingTest={
  _id:"123",
  name: "Super immeuble qui tue sa mère",
  latitude:48.850853542905114,
  longitude:2.343891862961394,
  address: "12 Boulevard du Général de Gaule",
  city : "Paris",
  description : "Un immeuble ultra boosté qui tue sa mère"
}









class App extends Component {

  render () {
    const myBuilding= historicalBuildingTest;
    return (
      <div>
          <HistoricalBuilding 
              _id={myBuilding._id}
              name={myBuilding.name}
              address={myBuilding.address}
              city={myBuilding.city}
              description={myBuilding.description}
          />
          < MapContainer historicalBuilding= {myBuilding}/>
      </div>
    ) 
  }
}


export default App;


