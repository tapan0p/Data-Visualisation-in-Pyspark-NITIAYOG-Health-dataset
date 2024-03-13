
import React, { useState, useEffect } from 'react';
import './Kmeans.css';

const Kmean = () => {
  const [selectedOption, setSelectedOption] = useState("kmeans1");
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
      <label htmlFor="options">Kmeans:</label>
      <select id="options" value={selectedOption} onChange={handleOptionChange}>
        <option value="kmeans1">plot 1</option>
        <option value="kmeans2">plot 2</option>
      </select>

      {selectedOption && (
        <div className="image-container">
          {plotImage && <img src={`data:image/png;base64,${plotImage}`} alt={`${selectedOption} Image`} />}
        </div>
      )}
    </div>
  );
};

export default Kmean;
