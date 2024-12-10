// src/App.js

import React from 'react';
import Artistas from './components/Artistas';
import Albuns from './components/Albuns';
import Musicas from './components/Musicas';

const App = () => {
  return (
    <div className="App">
      <h1>Music Library</h1>
      <Artistas />
      <Albuns />
      <Musicas />
    </div>
  );
};

export default App;