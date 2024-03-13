
import React, { useState, useEffect } from 'react';
import './Boxplot.css';

const Boxplot = () => {
  const [selectedOption, setSelectedOption] = useState("box1");
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
      <label htmlFor="options">Boxplot:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="box1">Stunted children under the age of 5 years (%)</option>
        <option value="box2">Wasted children under the age of 5 years (%)</option>
        <option value="box3">Underweight children under the age of 5 years (%)</option>
        <option value="box4">Children age group of 6 to 59 months with Mid-Upper Arm</option>
        <option value="box5">Children under the age group of 5 years with triceps skinfold (%)</option>
        <option value="box6">Children age group of 1 to 4 years with subscapular skinfold</option>
        <option value="box7">Stunned children age group of 5 to 9 years (%)</option>
        <option value="box8">Overweight or obese children age group of 5-9 years greater than +1 SD (%)</option>
        <option value="box9">Moderate or severely thin adolescents age group of 10 to 14 years</option>
        <option value="box10">Overweight or obese children age group of 5-9 years greater than +1 SD (%)</option>
      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Boxplot;
