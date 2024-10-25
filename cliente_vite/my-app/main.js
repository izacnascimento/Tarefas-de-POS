// src/main.js
import { getVehicleBrands, getModelsByBrand, getVehicleYears, getVehicleValue } from './counter';
import { createAccordionItem, displayModels, displayVehicleDetails } from './domManipulation.js';

document.getElementById('load-vehicles-btn').addEventListener('click', async () => {
    const brands = await getVehicleBrands();
    const vehicleAccordion = document.getElementById('vehicle-accordion');
    vehicleAccordion.innerHTML = ''; 

    brands.forEach((brand, index) => {
        const accordionItem = createAccordionItem(brand, index, async (brandCode, idx) => {
            const models = await getModelsByBrand(brandCode);
            displayModels(models.modelos, idx, async (modelCode, i, j) => {
                const years = await getVehicleYears(brandCode, modelCode);
                for (const year of years) {
                    const details = await getVehicleValue(brandCode, modelCode, year.codigo);
                    displayVehicleDetails(details, i, j);
                }
            });
        });
        vehicleAccordion.appendChild(accordionItem);
    });
});
