
import React, { useState, useEffect } from 'react';
import './Scatterplot.css';

const Scatterplot = () => {
  const [selectedOption, setSelectedOption] = useState("scatter1");
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
      <label htmlFor="options">Scatterplot:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="scatter1">Stunted children under the age of 5 years (%) , Severely stunted children under the age of 5 years (%)</option>
        <option value="scatter2">Wasted children under the age of 5 years (%) , Severely wasted children under the age of 5 years (%)</option>
        <option value="scatter3">Underweight children under the age of 5 years (%) , Severely underweight children under the age of 5 years (%)</option>
        <option value="scatter4">Stunned children age group of 5 to 9 years (%) , Severely stunted children age group of 5 to 9 years (%)</option>
      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Scatterplot;
