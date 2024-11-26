export async function getVehicleBrands() {
    const url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas';
    const response = await fetch(url);
    return await response.json();
  }
  
  export async function getModelsByBrand(brandCode) {
    const url = `https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos`;
    const response = await fetch(url);
    return await response.json();
  }
  
  export async function getVehicleYears(brandCode, modelCode) {
    const url = `https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos`;
    const response = await fetch(url);
    return await response.json();
  }
  
  export async function getVehicleValue(brandCode, modelCode, yearCode) {
    const url = `https://parallelum.com.br/fipe/api/v1/carros/marcas/${brandCode}/modelos/${modelCode}/anos/${yearCode}`;
    const response = await fetch(url);
    return await response.json();
  }
  