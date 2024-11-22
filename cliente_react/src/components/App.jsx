import React from 'react';
import Navbar from './components/Navbar';
import VehicleList from './components/App.jsx';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="container mt-5">
        <h2 className="text-center mb-4">Tabela de Veículos</h2>
        <VehicleList />
      </div>
    </div>
  );
}

export default App;
