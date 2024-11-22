// Hook para buscar os veículos
function useFetchVehicles() {
    const [vehicles, setVehicles] = useState([]);
    
    useEffect(() => {
        // Fetch da lista de veículos (clientes)
        async function fetchVehicles() {
            try {
                const response = await fetch('URL_DA_API_DE_VEICULOS');
                const data = await response.json();
                setVehicles(data); // Armazena os veículos no estado
            } catch (error) {
                console.error('Erro ao carregar os veículos:', error);
            }
        }

        fetchVehicles();
    }, []); 
    
    return vehicles;
}


function VehicleModelDetails({ brandCode, modelCode, index, modelIndex }) {
    const [modelDetails, setModelDetails] = useState([]);
    
    useEffect(() => {
        async function fetchModelDetails() {
            try {
                const anosResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos`);
                const anos = await anosResponse.json();
                
                const details = [];
                for (let ano of anos) {
                    const valorResponse = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos/${ano.codigo}`);
                    const valorData = await valorResponse.json();
                    details.push({ ano: ano.nome, valor: valorData.Valor });
                }
                setModelDetails(details);
            } catch (error) {
                console.error('Erro ao carregar os detalhes do modelo:', error);
            }
        }

        fetchModelDetails();
    }, [brandCode, modelCode]);

    return (
        <div className="model-details mt-2" id={`model-details-${index}-${modelIndex}`}>
            {modelDetails.map((detail, idx) => (
                <div key={idx}>
                    <p><strong>Ano:</strong> {detail.ano}</p>
                    <p><strong>Valor:</strong> {detail.valor}</p>
                    <hr />
                </div>
            ))}
        </div>
    );
}

// Componente para exibir os modelos de veículos
function VehicleModels({ brandCode, index }) {
    const [models, setModels] = useState([]);

    useEffect(() => {
        async function fetchModels() {
            try {
                const response = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos`);
                const data = await response.json();
                setModels(data.modelos);
            } catch (error) {
                console.error('Erro ao carregar os modelos:', error);
            }
        }

        fetchModels();
    }, [brandCode]);

    return (
        <div className="model-info mt-3">
            {models.map((model, modelIndex) => (
                <div key={modelIndex} className="model-item">
                    <p><strong>Modelo:</strong> {model.nome}</p>
                    <button className="btn btn-secondary btn-sm">
                        Mostrar Detalhes
                    </button>
                    <VehicleModelDetails brandCode={brandCode} modelCode={model.codigo} index={index} modelIndex={modelIndex} />
                </div>
            ))}
        </div>
    );
}

// Componente principal que exibe a lista de veículos
function VehicleAccordion() {
    const vehicles = useFetchVehicles();

    return (
        <div className="accordion" id="vehicle-accordion">
            {vehicles.map((vehicle, index) => (
                <div className="accordion-item" key={index}>
                    <h2 className="accordion-header" id={`heading-${index}`}>
                        <button
                            className="accordion-button collapsed"
                            type="button"
                            data-bs-toggle="collapse"
                            data-bs-target={`#collapse-${index}`}
                            aria-expanded="false"
                            aria-controls={`collapse-${index}`}
                        >
                            {vehicle.clientName}
                        </button>
                    </h2>
                    <div
                        id={`collapse-${index}`}
                        className="accordion-collapse collapse"
                        aria-labelledby={`heading-${index}`}
                        data-bs-parent="#vehicle-accordion"
                    >
                        <div className="accordion-body" id={`vehicle-details-${index}`}>
                            <button className="btn btn-info">Mostrar Modelos</button>
                            <VehicleModels brandCode={vehicle.code} index={index} />
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default VehicleAccordion;
