import React from 'react'
import PropTypes from 'prop-types'


const HistoricalBuilding= ({building}) => (
    <div className={`historicalBuilding ${building.name}`}>
        <span property="specify an RDF property">
            
             <h3 property="specify RDF name">{building.name}</h3>
            
            <p property="specify RDF description">
                {building.description}
            </p>
            <p property="specify RDF adress">
                <em>{building.address}, {building.city}</em>
            </p>
        </span>
    </div>

)

HistoricalBuilding.propTypes={
    building : PropTypes.object.isRequired,
}


export default HistoricalBuilding