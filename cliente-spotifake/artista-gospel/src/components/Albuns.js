// src/components/Albuns.js

import React, { useEffect, useState } from 'react';
import { api } from '../api/api.js';

const Albuns = () => {
  const [albuns, setAlbuns] = useState([]);
  const [artistaId, setArtistaId] = useState('');
  const [nome, setNome] = useState('');
  const [ano, setAno] = useState('');

  useEffect(() => {
    const fetchAlbuns = async () => {
      const data = await api.fetchData('albuns/');
      setAlbuns(data);
    };
    fetchAlbuns();
  }, []);

  const handleAddAlbum = async () => {
    const newAlbum = { artista: artistaId, nome, ano };
    const addedAlbum = await api.postData('albuns/', newAlbum);
    setAlbuns([...albuns, addedAlbum]);
  };

  return (
    <div>
      <h2>Álbuns</h2>
      <ul>
        {albuns.map((album) => (
          <li key={album.id}>
            {album.nome} ({album.ano}) - Artista: {album.artista}
          </li>
        ))}
      </ul>
      <div>
        <h3>Adicionar Álbum</h3>
        <input
          type="text"
          placeholder="Nome"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="number"
          placeholder="Ano"
          value={ano}
          onChange={(e) => setAno(e.target.value)}
        />
        <input
          type="number"
          placeholder="ID do Artista"
          value={artistaId}
          onChange={(e) => setArtistaId(e.target.value)}
        />
        <button onClick={handleAddAlbum}>Adicionar</button>
      </div>
    </div>
  );
};

export default Albuns;