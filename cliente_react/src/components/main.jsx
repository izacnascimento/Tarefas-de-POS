import React, { useState } from 'react';

function VehicleList() {
  const [vehicles, setVehicles] = useState([]);
  const [loading, setLoading] = useState(false);

  // Função para carregar os veículos da API
  async function loadVehicles() {
    setLoading(true);
    try {
      const response = await fetch('https://parallelum.com.br/fipe/api/v1/motos/marcas');
      const brands = await response.json();
      setVehicles(brands.map(brand => ({
        clientName: brand.nome,
        code: brand.codigo
      })));
    } catch (error) {
      console.error('Erro ao buscar os veículos:', error);
      alert('Não foi possível carregar os veículos.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <div className="d-grid gap-2 col-6 mx-auto mb-4">
        <button className="btn btn-primary btn-lg" onClick={loadVehicles} disabled={loading}>
          {loading ? 'Carregando...' : 'Buscar Veículos'}
        </button>
      </div>

      <div className="accordion" id="vehicle-accordion">
        {vehicles.length > 0 && vehicles.map((vehicle, index) => (
          <div className="accordion-item" key={vehicle.code}>
            <h2 className="accordion-header" id={`heading-${index}`}>
              <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target={`#collapse-${index}`} aria-expanded="false" aria-controls={`collapse-${index}`}>
                {vehicle.clientName}
              </button>
            </h2>
            <div id={`collapse-${index}`} className="accordion-collapse collapse" aria-labelledby={`heading-${index}`} data-bs-parent="#vehicle-accordion">
              <div className="accordion-body">
                <button className="btn btn-info" onClick={() => loadModels(vehicle.code, index)}>
                  Mostrar Modelos
                </button>
                <div className="model-info mt-3" id={`vehicle-details-${index}`}></div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  // Função para carregar os modelos de uma marca
  async function loadModels(brandCode, index) {
    try {
      const modelsResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/motos/marcas/${brandCode}/modelos`);
      const models = await modelsResponse.json();

      const modelInfo = document.querySelector(`#vehicle-details-${index}`);
      modelInfo.innerHTML = '';

      models.modelos.forEach((model) => {
        const modelItem = document.createElement('div');
        modelItem.innerHTML = `
          <p><strong>Modelo:</strong> ${model.nome}</p>
          <button class="btn btn-secondary btn-sm" onclick="loadModelDetails(${brandCode}, ${model.codigo}, ${index}, ${model.codigo})">Mostrar Detalhes</button>
          <div id="model-details-${index}-${model.codigo}" class="mt-2"></div>
        `;
        modelInfo.appendChild(modelItem);
      });
    } catch (error) {
      console.error('Erro ao carregar os modelos:', error);
      alert('Não foi possível carregar os modelos.');
    }
  }

  // Função para carregar os detalhes de um modelo específico
  async function loadModelDetails(brandCode, modelCode, index, modelIndex) {
    try {
      const anosResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/motos/marcas/${brandCode}/modelos/${modelCode}/anos`);
      const anos = await anosResponse.json();

      const modelDetails = document.querySelector(`#model-details-${index}-${modelIndex}`);
      modelDetails.innerHTML = '';

      anos.forEach((ano) => {
        modelDetails.innerHTML += `
          <p><strong>Ano:</strong> ${ano.nome}</p>
        `;
      });
    } catch (error) {
      console.error('Erro ao carregar os detalhes do modelo:', error);
      alert('Não foi possível carregar os detalhes do modelo.');
    }
  }
}

export default VehicleList;

