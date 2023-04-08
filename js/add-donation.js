const validarForm = () => {
    //funciones auxiliares
    const validarNombre = (nombre) => nombre && nombre.length > 2 && nombre.length < 81;
    const validarEmail = (email) => /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/gm.test(email);
    const validarTelefono = (telefono) => !telefono || /^\+569[0-9]{8}$/gm.test(telefono);
    //parte con +569 le siguen exactamente 8 numeros y termina
    const validarExiste = (x) => x && true;

    //obtener inputs
    let regioninput = document.getElementById("region"); 
    let comunainput = document.getElementById("comuna");
    let calleinput = document.getElementById("calle-numero");
    let tipoinput = document.getElementById("tipo-donacion");
    let cantidadinput = document.getElementById("cantidad");
    let fechainput = document.getElementById("fecha");
    //let descripcioninput = document.getElementById("descripcion");
    //let condicionesinput = document.getElementById("codiciones-retiro");
    let fotoinput = document.getElementById("foto-donacion");
    let nombreinput = document.getElementById("nombre");
    let emailinput = document.getElementById("email");
    let celularinput = document.getElementById("celular");



}