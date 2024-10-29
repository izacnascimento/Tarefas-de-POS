function displayVehicles(vehicleList) {
    const vehicleAccordion = document.getElementById('vehicle-accordion');
    vehicleAccordion.innerHTML = ''; 

    vehicleList.forEach((vehicle, index) => {
        const accordionItem = document.createElement('div');
        accordionItem.className = 'accordion-item';

        accordionItem.innerHTML = `
            <h2 class="accordion-header" id="heading-${index}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${index}" aria-expanded="false" aria-controls="collapse-${index}">
                    ${vehicle.clientName}
                </button>
            </h2>
            <div id="collapse-${index}" class="accordion-collapse collapse" aria-labelledby="heading-${index}" data-bs-parent="#vehicle-accordion">
                <div class="accordion-body" id="vehicle-details-${index}">
                    <button class="btn btn-info" onclick="loadModels(${vehicle.code}, ${index})">Mostrar Modelos</button>
                    <div class="model-info mt-3"></div> <!-- Local onde os modelos serão exibidos -->
                </div>
            </div>
        `;

        vehicleAccordion.appendChild(accordionItem);
    });
}

async function loadModels(brandCode, index) {
    try {
        const modelsResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos`);
        const models = await modelsResponse.json();

        const modelInfo = document.querySelector(`#vehicle-details-${index} .model-info`);
        modelInfo.innerHTML = '';


        models.modelos.forEach((model, modelIndex) => {
            const modelItem = document.createElement('div');
            modelItem.className = 'model-item';

            modelItem.innerHTML = `
                <p><strong>Modelo:</strong> ${model.nome} 
                    <button class="btn btn-secondary btn-sm" onclick="loadModelDetails(${brandCode}, ${model.codigo}, ${index}, ${modelIndex})">Mostrar Detalhes</button>
                </p>
                <div class="model-details mt-2" id="model-details-${index}-${modelIndex}"></div>
            `;
            modelInfo.appendChild(modelItem);
        });
    } catch (error) {
        console.error('Erro ao carregar os modelos:', error);
        alert('Não foi possível carregar os modelos.');
    }
}


async function loadModelDetails(brandCode, modelCode, index, modelIndex) {
    try {
        const anosResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos`);
        const anos = await anosResponse.json();

        const modelDetails = document.querySelector(`#model-details-${index}-${modelIndex}`);
        modelDetails.innerHTML = ''; 

        for (let ano of anos) {
           
            const valorResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos/${ano.codigo}`);
            const valorData = await valorResponse.json();

            modelDetails.innerHTML += `
                <p><strong>Ano:</strong> ${ano.nome}</p>
                <p><strong>Valor:</strong> ${valorData.Valor}</p>
                <hr>
            `;
        }
    } catch (error) {
        console.error('Erro ao carregar os detalhes do modelo:', error);
        alert('Não foi possível carregar os detalhes do modelo.');
    }
}

window.loadModels = loadModels;
window.loadModelDetails = loadModelDetails;
