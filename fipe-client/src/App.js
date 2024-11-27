import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import VehicleAccordion from './components/VehicleAccordion'; 
import Contato from './pages/Contato.js'; 
import './App.css'; 

const App = () => {
  return (
    <Router> 
      <div className="App">
        <h1>Consulta FIPE - Carros</h1>
        
        {/* Definindo as rotas */}
        <Routes>
          <Route path="/" element={<VehicleAccordion />} /> {/* Página inicial */}
          <Route path="/contato" element={<Contato />} /> {/* Contato */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
