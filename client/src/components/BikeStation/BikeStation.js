import React from 'react'
import PropTypes from 'prop-types'



// component Museum used to render a museum data gotten from the source
// and specify its rdf properties in the web app
// the museum props is an object containing all information about museum

const BikeStation= ({station}) => (
    <div className={`Station ${building.name}`}>
        <span property="specify an RDF property">
            
             <h3 property="specify RDF name">{station.name}</h3>
            
            <p property="specify RDF description">
                {station.description}
            </p>
            <p property="Specify RDF specs">
                Number of available bikes : {station.availableBikes}
                Number of free slots : {station.freeSlots}
            </p>

            <p property="specify RDF adress">
                <em>{museum.address}, {museum.city}</em>
            </p>

        </span>
    </div>

)

BikeStation.propTypes={
    station : PropTypes.object.isRequired,
}


export default BikeStation