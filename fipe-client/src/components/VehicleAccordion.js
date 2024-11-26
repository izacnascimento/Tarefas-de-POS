import React, { useEffect, useState } from 'react';
import { getVehicleBrands } from '../api/api';
import VehicleModelDetails from './VehicleModelDetails';

const VehicleAccordion = () => {
  const [brands, setBrands] = useState([]);

  useEffect(() => {
    async function fetchBrands() {
      const brandsData = await getVehicleBrands();
      setBrands(brandsData);
    }
    fetchBrands();
  }, []);

  return (
    <div className="accordion" id="vehicle-accordion">
      {brands.map((brand, index) => (
        <div key={index} className="accordion-item">
          <h2 className="accordion-header" id={`heading-${index}`}>
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target={`#collapse-${index}`}
              aria-expanded="false"
              aria-controls={`collapse-${index}`}
            >
              {brand.nome}
            </button>
          </h2>
          <div
            id={`collapse-${index}`}
            className="accordion-collapse collapse"
            aria-labelledby={`heading-${index}`}
            data-bs-parent="#vehicle-accordion"
          >
            <div className="accordion-body">
              <VehicleModelDetails brandCode={brand.codigo} />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default VehicleAccordion;
