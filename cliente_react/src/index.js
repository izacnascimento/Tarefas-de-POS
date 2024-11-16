

document.getElementById('load-vehicles-btn').addEventListener('click', loadVehicles);

async function loadVehicles() {
    try {
        const url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'; 
        const response = await fetch(url);
        const brands = await response.json();

        // Mapeia as marcas para veículos
        const vehicles = brands.map(brand => ({
            clientName: brand.nome,
            code: brand.codigo
        }));

        displayVehicles(vehicles); 
    } catch (error) {
        console.error('Erro ao buscar os veículos:', error);
        alert('Não foi possível carregar os veículos.');
    }
}
