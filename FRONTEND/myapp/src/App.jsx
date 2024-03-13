import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import './components/Histogram'
import Histogram from './components/Histogram';
import Boxplot from './components/Boxplot';
import Scatterplot from './components/Scatterplot';
import Pi from './components/Pi';
import Lineplot from './components/Lineplot';
import LR from './components/LR';
import Kmean from './components/Kmeans';
import GMM from './components/GMM'
import Co from './components/Co'


function App() {

  return (
    <div className="front-page-container">
      <nav className="navbar">
        <div className="header">
          <div className="logo">
            <img src="\src\assets\IITG_logo.png" alt="Your Logo" />
          </div>
          <h3>Data Visualisation in Pyspark : NITIAYOG Health dataset</h3>
          <p>Group Members:</p> 
          <p> Tapan Mahata 234161010</p> <p> Diganta Diasi 234161004 </p> <p>Dev Wankhede 234161003</p>
        </div>
        
      </nav>

      <div className="body">
        <Histogram></Histogram>
        <Boxplot></Boxplot>
        <Scatterplot></Scatterplot>
        <Pi></Pi>
        <LR></LR>
        <Kmean></Kmean>
        <GMM></GMM>

      </div>
    </div>
  );
}

export default App;
