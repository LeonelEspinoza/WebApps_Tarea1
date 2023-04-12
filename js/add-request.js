const validarForm = () => {
    //funciones auxiliares
    const validarNombre = (nombre) => nombre && nombre.length > 2 && nombre.length < 81;
    const validarEmail = (email) => /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/gm.test(email);
    const validarTelefono = (telefono) => !telefono || /^\+569[0-9]{8}$/gm.test(telefono);
    //parte con +569 le siguen exactamente 8 numeros y termina
    const validarExiste = (x) => x && true;
    const validarDescripcion = (desc) => desc.length < 250;
    const validarTipo = (tipo) => tipo && (tipo == "fruta" || tipo == "verdura" || tipo == "otro");
    //obtener inputs
    let regioninput = document.getElementById("region"); 
    let comunainput = document.getElementById("comuna");
    let tipoinput = document.getElementById("tipo-pedido");
    let descripcioninput = document.getElementById("descripcion");
    let cantidadinput = document.getElementById("cantidad");
    let nombreinput = document.getElementById("nombre");
    let emailinput = document.getElementById("email");
    let celularinput = document.getElementById("celular");

    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");

    let isValid = false;
    let InvalidInputs = [];


    const setInvalidInput = (inputName) =>{
        InvalidInputs.push(inputName);
        isValid&&=false;
    }

    if (!validarExiste(regioninput.value)) {
        setInvalidInput("Región");
    }

    if (!validarExiste(comunainput.value)) {
        setInvalidInput("Comuna");
    }

    if (!validarTipo(tipoinput.value)) {
        setInvalidInput("Tipo pedido");
    }

    if (!validarDescripcion(descripcioninput.value)) {
        setInvalidInput("Decripción pedido");
    }

    if (!validarExiste(cantidadinput.value)) {
        setInvalidInput("Cantidad");
    }

    if (!validarNombre(nombreinput.value)) {
        //msg += "El largo del nombre debe ser entre 2 y 80 caracteres\n";
        setInvalidInput("Nombre solicitante");
    } 

    if (!validarEmail(emailinput.value)) {
            //msg += "Email Incorrecto\n";
            setInvalidInput("Email solicitante");
    }

    if (!validarTelefono(celularinput.value)) {
            //msg += "Telefono Incorrecto\n";
            setInvalidInput("Número celular solicitante");
    }
    
    if (!isValid){
        validationListElem.textContent = "";
        for (input of InvalidInputs){
            let listElement = document.createElement("li");
            listElement.innerText = input;
            validationListElem.append(listElement);
        }
        validationMessageElem.innerText = "Corregir los siguientes campos:";
        validationBox.hidden = false;
    } else {
        if (confirm("¿Confirma que desea agregar este pedido?")){
            alert("Hemos recibido la informacion de su pedido. Muchas gracias.");
            window.location.href = "../html/inicio.html";
        }
    }
};

let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);