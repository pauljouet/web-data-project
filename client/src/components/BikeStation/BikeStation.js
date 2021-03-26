import './BikeStation.css'

import React from 'react'
import PropTypes from 'prop-types'



// component Museum used to render a museum data gotten from the source
// and specify its rdf properties in the web app
// the museum props is an object containing all information about museum

const BikeStation= ({station}) => (
    <div className="bikeStation-container">
        <span>
            
             <h3 property="ns:hasName">🚲 {station.name}</h3>

            <p>
                <li>Total bike capacity : <em property="ns:hasCapacity">{station.cap}</em></li>
                <li>Number of available bikes : <em property="ns:hasAvailableBikes">{station.avbikes}</em></li>
                <li>Number of free slots : <em property="ns:hasAvailableDocks">{station.avdocks}</em></li>
            </p>

        </span>
    </div>

)

BikeStation.propTypes={
    station : PropTypes.object.isRequired,
}


export default BikeStation