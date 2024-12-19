// src/components/Musicas.js

import React, { useEffect, useState } from 'react';
import { api } from '../api/api.js';

const Musicas = () => {
  const [musicas, setMusicas] = useState([]);
  const [albumId, setAlbumId] = useState('');
  const [nome, setNome] = useState('');
  const [segundos, setSegundos] = useState('');

  useEffect(() => {
    const fetchMusicas = async () => {
      const data = await api.fetchData('musicas/');
      setMusicas(data);
    };
    fetchMusicas();
  }, []);

  const handleAddMusica = async () => {
    const newMusica = { album: albumId, nome, segundos };
    const addedMusica = await api.postData('musicas/', newMusica);
    setMusicas([...musicas, addedMusica]);
  };

  return (
    <div>
      <h2>Músicas</h2>
      <ul>
        {musicas.map((musica) => (
          <li key={musica.id}>
            {musica.nome} - {musica.segundos}s - Álbum: {musica.album}
          </li>
        ))}
      </ul>
      <div>
        <h3>Adicionar Música</h3>
        <input
          type="text"
          placeholder="Nome"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="number"
          placeholder="Segundos"
          value={segundos}
          onChange={(e) => setSegundos(e.target.value)}
        />
        <input
          type="number"
          placeholder="ID do Álbum"
          value={albumId}
          onChange={(e) => setAlbumId(e.target.value)}
        />
        <button onClick={handleAddMusica}>Adicionar</button>
      </div>
    </div>
  );
};

export default Musicas;