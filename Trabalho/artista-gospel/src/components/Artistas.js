// src/components/Artistas.js

import React, { useEffect, useState } from 'react';
import { api } from '../api/api';

const Artistas = () => {
  const [artistas, setArtistas] = useState([]);
  const [nome, setNome] = useState('');
  const [local, setLocal] = useState('');
  const [anoCriacao, setAnoCriacao] = useState('');

  useEffect(() => {
    const fetchArtistas = async () => {
      const data = await api.fetchData('artistas/');
      setArtistas(data);
    };
    fetchArtistas();
  }, []);

  const handleAddArtista = async () => {
    const newArtista = { nome, local, ano_criacao: anoCriacao };
    const addedArtista = await api.postData('artistas/', newArtista);
    setArtistas([...artistas, addedArtista]);
  };

  return (
    <div>
      <h2>Artistas</h2>
      <ul>
        {artistas.map((artista) => (
          <li key={artista.id}>
            {artista.nome} ({artista.local}) - {artista.ano_criacao}
          </li>
        ))}
      </ul>
      <div>
        <h3>Adicionar Artista</h3>
        <input
          type="text"
          placeholder="Nome"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
        <input
          type="text"
          placeholder="Local"
          value={local}
          onChange={(e) => setLocal(e.target.value)}
        />
        <input
          type="number"
          placeholder="Ano de Criação"
          value={anoCriacao}
          onChange={(e) => setAnoCriacao(e.target.value)}
        />
        <button onClick={handleAddArtista}>Adicionar</button>
      </div>
    </div>
  );
};

export default Artistas;