// src/App.js

import React from 'react';
import Artistas from './components/Artistas.js';
import Albuns from './components/Albuns.js';
import Musicas from './components/Musicas.js';

const App = () => {
  return (
    <div className="App">
      <h1>Biblioteca de Música</h1>
      <Artistas />
      <Albuns />
      <Musicas />
    </div>
  );
};

export default App;