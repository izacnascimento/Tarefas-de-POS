import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'cliente_react';  // Importando React Router
import Header from './components/Header';  // Importando o Header
import './App.css';

function App() {
  return (
    <Router>
      <Header />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<h2>Bem-vindo à página inicial</h2>} />
          <Route path="/sobre" element={<h2>Sobre o site</h2>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
