import React, { useState } from 'react';
import { getModelsByBrand, getVehicleYears, getVehicleValue } from '../api/api';

const VehicleModelDetails = ({ brandCode }) => {
  const [models, setModels] = useState([]);
  const [vehicleDetails, setVehicleDetails] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadModels = async () => {
    setLoading(true);
    const modelsData = await getModelsByBrand(brandCode);
    setModels(modelsData.modelos);
    setLoading(false);
  };

  const loadModelDetails = async (modelCode) => {
    const yearsData = await getVehicleYears(brandCode, modelCode);
    const details = await Promise.all(
      yearsData.map(async (year) => {
        const valueData = await getVehicleValue(brandCode, modelCode, year.codigo);
        return { year, value: valueData.Valor };
      })
    );
    setVehicleDetails(details);
  };

  return (
    <div>
      <button className="btn btn-info" onClick={loadModels}>
        Mostrar Modelos
      </button>

      {loading ? (
        <p>Carregando modelos...</p>
      ) : (
        <div>
          {models.map((model) => (
            <div key={model.codigo}>
              <p>
                <strong>Modelo:</strong> {model.nome}
                <button
                  className="btn btn-secondary btn-sm"
                  onClick={() => loadModelDetails(model.codigo)}
                >
                  Mostrar Detalhes
                </button>
              </p>
            </div>
          ))}
        </div>
      )}

      <div>
        {vehicleDetails.map((detail, index) => (
          <div key={index}>
            <p>
              <strong>Ano:</strong> {detail.year.nome} <br />
              <strong>Valor:</strong> {detail.value}
            </p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
};

export default VehicleModelDetails;
