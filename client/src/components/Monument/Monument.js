import './Monument.css'

import React from 'react'
import PropTypes from 'prop-types'


const Monument= ({monument}) => (
    <div className="monument-container">
        <span property="specify an RDF property">
            
             <h3 property="specify RDF name">🗽 {monument.name}</h3>
            
            <p property="specify RDF description">
                {monument.descr}
            </p>
            <p property="specify RDF adress">
                <em>{monument.city}</em>
            </p>
        </span>
    </div>

)

Monument.propTypes={
    monument : PropTypes.object.isRequired,
}


export default Monument