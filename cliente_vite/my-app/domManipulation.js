// src/domManipulation.js

export function createAccordionItem(vehicle, index, onClickShowModels) {
    const accordionItem = document.createElement('div');
    accordionItem.className = 'accordion-item';

    accordionItem.innerHTML = `
        <h2 class="accordion-header" id="heading-${index}">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                ${vehicle.nome}
            </button>
        </h2>
        <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#vehicle-accordion">
            <div class="accordion-body" id="vehicle-details-${index}">
                <button class="btn btn-info" onclick="onClickShowModels(${vehicle.codigo}, ${index})">Mostrar Modelos</button>
                <div class="model-info mt-3"></div>
            </div>
        </div>
    `;
    return accordionItem;
}

export function displayModels(models, index, onClickShowDetails) {
    const modelInfo = document.querySelector(`#vehicle-details-${index} .model-info`);
    modelInfo.innerHTML = '';

    models.forEach((model, modelIndex) => {
        const modelItem = document.createElement('div');
        modelItem.className = 'model-item';

        modelItem.innerHTML = `
            <p><strong>Modelo:</strong> ${model.nome} 
                <button class="btn btn-secondary btn-sm" onclick="onClickShowDetails(${model.codigo}, ${index}, ${modelIndex})">Mostrar Detalhes</button>
            </p>
            <div class="model-details mt-2" id="model-details-${index}-${modelIndex}"></div>
        `;
        modelInfo.appendChild(modelItem);
    });
}

export function displayVehicleDetails(details, index, modelIndex) {
    const modelDetails = document.querySelector(`#model-details-${index}-${modelIndex}`);
    modelDetails.innerHTML = `
        <p><strong>Ano:</strong> ${details.anoModelo}</p>
        <p><strong>Valor:</strong> ${details.Valor}</p>
        <hr>
    `;
}
