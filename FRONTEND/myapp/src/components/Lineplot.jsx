
import React, { useState, useEffect } from 'react';
import './Lineplot.css';

const Lineplot = () => {
  const [selectedOption, setSelectedOption] = useState("lineplot1");
  const [plotImage, setPlotImage] = useState('');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  useEffect(() => {
    const fetchImage = async () => {
      if (selectedOption) {
        const response = await fetch(`http://localhost:5000/${selectedOption}`);
        const data = await response.json();
        setPlotImage(data.plot);
      }
    };

    fetchImage();
  }, [selectedOption]);

  return (
    <div className="dropdown-container">
      <label htmlFor="options">Lineplot:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="lineplot1">Year , Stunted children under the age of 5 years (%) </option>
        <option value="lineplot2">Year , Severely stunted children under the age of 5 years (%) </option>
      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Lineplot;
