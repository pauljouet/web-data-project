import React, { useState } from "react";
import "./FilterButtons.css";

const FilterButtons = ({ buttons, doSomethingAfterClick }) => {
  const [clickedId, setClickedId] = useState(-1);

  const handleClick = (event, id) => {
    setClickedId(id);
    doSomethingAfterClick(event);
  };

  return (
    <>
      {buttons.map((buttonLabel, i) => (
        <button
          key={i}
          name={buttonLabel}
          onClick={(event) => handleClick(event, i)}
          className={i === clickedId ? "filterButton active" : "filterButton"}
        >
          {buttonLabel}
        </button>
      ))}
    </>
  );
};

export default FilterButtons;
