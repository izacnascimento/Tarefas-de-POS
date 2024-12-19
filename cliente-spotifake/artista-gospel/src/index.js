// src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/App.css';
import App from './app';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);
root.render(<App />);