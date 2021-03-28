import './Museum.css'

import React from 'react'
import PropTypes from 'prop-types'



// component Museum used to render a museum data gotten from the source
// and specify its rdf properties in the web app
// the museum props is an object containing all information about museum

const Museum= ({museum}) => (
    <div className="museum-container">
        <span>
            
             <h3 property="ns:hasName">🏛 {museum.name}</h3>
            
            <p property="ns:hasWebsite">
                <a>{museum.wb}</a>
            </p>
            <p>
                Adresse : <em property="ns: hasAdress">{museum.address}</em>,
                <em property="hasCity"> {museum.city}</em>
            </p>

        </span>
    </div>

)

Museum.propTypes={
    museum : PropTypes.object.isRequired,
}


export default Museum