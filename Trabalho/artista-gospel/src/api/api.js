// src/api/api.js

const BASE_URL = 'http://localhost:8000/';  // Substitua pela URL do seu backend

const fetchData = async (endpoint) => {
  const response = await fetch(BASE_URL + endpoint);
  const data = await response.json();
  return data;
};

const postData = async (endpoint, data) => {
  const response = await fetch(BASE_URL + endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return await response.json();
};

const putData = async (endpoint, data) => {
  const response = await fetch(BASE_URL + endpoint, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return await response.json();
};

const deleteData = async (endpoint) => {
  const response = await fetch(BASE_URL + endpoint, {
    method: 'DELETE',
  });
  return await response.json();
};

export const api = {
  fetchData,
  postData,
  putData,
  deleteData,
};