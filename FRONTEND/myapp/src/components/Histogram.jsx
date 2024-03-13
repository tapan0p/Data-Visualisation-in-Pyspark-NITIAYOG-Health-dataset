// Histogram.js

import React, { useState, useEffect } from 'react';
import './Histogram.css'; // Import your CSS file for styling

const Histogram = () => {
  const [selectedOption, setSelectedOption] = useState("hist1");
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
      <label htmlFor="options">Histogram:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="hist1">Stunted children under the age of 5 years (%)</option>
        <option value="hist2">Wasted children under the age of 5 years (%)</option>
        <option value="hist3">Underweight children under the age of 5 years (%)</option>
        <option value="hist4">Children age group of 6 to 59 months with Mid-Upper Arm Circumference ( MUAC ) less than 125 cm (%)</option>
        <option value="hist5">Children under the age group of 5 years with triceps skinfold (%) less than -2 SD (%)</option>
        <option value="hist6">Children age group of 1 to 4 years with subscapular skinfold less than -2 SD (%)</option>
        <option value="hist7">Stunned children age group of 5 to 9 years (%)</option>
        <option value="hist8">Overweight or obese children age group of 5-9 years greater than +1 SD (%)</option>
        <option value="hist9">Moderate or severely thin adolescents age group of 10 to 14 years</option>
        <option value="hist10">Overweight or obese children age group of 5-9 years greater than +1 SD (%)</option>
      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Histogram;
