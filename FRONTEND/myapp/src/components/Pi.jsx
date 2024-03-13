
import React, { useState, useEffect } from 'react';
import './Pi.css';

const Pi = () => {
  const [selectedOption, setSelectedOption] = useState("piplot1");
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
      <label htmlFor="options">Pichart:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="piplot1">Stunted children under the age of 5 years (%) , Residence type</option>
        <option value="piplot2">Underweight children under the age of 5 years (%) , State</option>
        <option value="piplot3">Wasted children under the age of 5 years (%) , Residence type</option>
        <option value="piplot4">Severely stunted children under the age of 5 years (%) , Residence type</option>
        <option value="piplot5">Wasted children under the age of 5 years (%) , State</option>
        <option value="piplot6">Children age group of 6 to 59 months with Mid-Upper Arm Circumference ( MUAC ) less than -3 SD (%) , State</option>

      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Pi;
