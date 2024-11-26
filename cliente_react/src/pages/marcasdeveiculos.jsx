import React, { useState, useEffect } from 'react';
import { loadMarcas, filterMarcas } from '../services/Veiculosmarcas.js';

const marcasdeveiculos = () => {
    const [marcas, setMarcas] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [filteredMarcas, setFilteredMarcas] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const handleLoadMarcas = async () => {
        try {
            const data = await loadMarcas();
            setMarcas(data);
            setFilteredMarcas(data);
        } catch (error) {
            console.error('Erro ao carregar marcas:', error);
        }
    };

    useEffect(() => {
        setFilteredMarcas(filterMarcas(marcas, searchQuery));
    }, [searchQuery, marcas]);

    return (
        <div className="px-4 py-3 my-5 text-center">
            <div className="container mt-5">
                <h2>Marcas do Carros</h2>

                <table className="table table-striped table-hover table-bordered">
                    <thead className="table-dark">
                        <tr>
                            <th>Id do carro</th>
                            <th>Marcas do Carro</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredMarcas.map((marca) => (
                            <tr key={marca.codigo}>
                                <td>{marca.codigo}</td>
                                <td>{marca.nome}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>

                <button
                    className="btn btn-primary rounded-pill px-3"
                    onClick={handleLoadMarcas}>
                    {isLoading ? 'Carregando...' : 'Solicitar as informações sobre a Marcas'}
                </button>
            </div>
        </div>
    );
};

export default marcasdeveiculos;