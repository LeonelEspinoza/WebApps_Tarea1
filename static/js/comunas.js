import region_comuna from "../region_comuna.json"

const regionselect = document.getElementById("region");
const comunaselect = document.getElementById("comuna");

regionselect.addEventListener("change", event => {
    comunaselect.innerHTML = "<option selected disabled>Elegir comuna</option>";

    const regionvalue = event.taget.value;

 const region = region_comuna.find(region => region.id == regionvalue);
    
    region.comunas.forEach(comuna => {
        const option = document.createElement("option");
        option.value = comuna.id;
        option.textContent = comuna.nombre;
        comunaselect.appendChild(option);
    });
});




// //Mostrar las comunas de la región seleccionada
// regionSelect.addEventListener("change", e => {
//     // Limpiar las opciones del select de comunas
//     comunaSelect.innerHTML = "<option selected disabled>Seleccione una comuna</option>";

//     const regionId = e.target.value;
//     const region = regiones.find(region => region.id == regionId);
//     region.comunas.forEach(comuna => {
//         const option = document.createElement("option");
//         option.value = comuna.id;
//         option.textContent = comuna.nombre;
//         comunaSelect.appendChild(option);
//     });
// });