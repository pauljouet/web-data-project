import React from 'react'
import PropTypes from 'prop-types'


const HistoricalBuilding= ({_id, name, address, city, description}) => (
    <div className={`historicalBuilding ${name}`}>
        <span property="specify an RDF property">
            <p property="specify RDF name">
                <h3>{name}</h3>
            </p>
            <p property="specify RDF description">
                {description}
            </p>
            <p property="specify RDF adress">
                <em>{address}, {city}</em>
            </p>
        </span>
    </div>

)

HistoricalBuilding.propTypes={
    _id : PropTypes.string.isRequired,
    name : PropTypes.string.isRequired,
    address : PropTypes.string.isRequired,
    city : PropTypes.string.isRequired,
    description : PropTypes.string
}


export default HistoricalBuilding