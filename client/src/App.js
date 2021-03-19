import './App.css';
import React, {Component} from 'react'

import {HistoricalBuilding} from './components'

const historicalBuildingTest={
  _id:"123",
  name: "Super immeuble qui tue sa mère",
  address: "12 Boulevard du Général de Gaule",
  city : "Paris",
  description : "Un immeuble ultra boosté qui tue sa mère"

}

class App extends Component {

  render () {
    const {_id, name, address, city, description}= historicalBuildingTest
    return (
      <div>
          <HistoricalBuilding 
              _id={_id}
              name={name}
              address={address}
              city={city}
              description={description}
          />
      </div>
    

    ) 
  }
}

export default App;
