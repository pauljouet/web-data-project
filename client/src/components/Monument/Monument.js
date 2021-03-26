import './Monument.css'

import React from 'react'
import PropTypes from 'prop-types'


const Monument= ({monument}) => (
    <div className="monument-container">
        <span >     
             <h3 property="ns:hasName">🗽 {monument.name}</h3>        
            <p property="ns:hasDescription">
                {monument.descr}
            </p>
            <p property="ns:hasCity">
                <em>{monument.city}</em>
            </p>
        </span>
    </div>

)

Monument.propTypes={
    monument : PropTypes.object.isRequired,
}


export default Monument