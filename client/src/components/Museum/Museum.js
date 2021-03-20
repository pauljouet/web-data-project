import React from 'react'
import PropTypes from 'prop-types'



// component Museum used to render a museum data gotten from the source
// and specify its rdf properties in the web app
// the museum props is an object containing all information about museum

const Museum= ({museum}) => (
    <div className={`Museum ${building.name}`}>
        <span property="specify an RDF property">
            
             <h3 property="specify RDF name">{museum.name}</h3>
            
            <p property="specify RDF description">
                {museum.description}
            </p>
            <p property="specify RDF adress">
                <em>{museum.address}, {museum.city}</em>
                Horaire d'ouvertures : <em>{museum.openingTime}</em>
            </p>

        </span>
    </div>

)

Museum.propTypes={
    museum : PropTypes.object.isRequired,
}


export default Museum