let photos=1;

const validarForm = () => {
    //funciones auxiliares
    const validarNombre = (nombre) => nombre && nombre.length > 2 && nombre.length < 81;
    const validarEmail = (email) => /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/gm.test(email);
    const validarTelefono = (telefono) => !telefono || /^\+569[0-9]{8}$/gm.test(telefono);
    //parte con +569 le siguen exactamente 8 numeros y termina
    const validarExiste = (x) => x && true;
    const validarFotos = (files) => {
        if (!files) return false;
        let lengthValid = 1<=files.length && files.length <= 3;
        let typeValid = true
        for (const file of files){
            let fileFamily = file.type.split("/") [0];
            typeValid &&= fileFamily =="image" || file.type == "aplication/pdf";
        }
        return typeValid && lengthValid;

    }
    
    //const validarFecha = (fecha) => {
    //    /^[0-9]{2}\-((0(1|[3-9])|1[0-2])\-(0[1-9]|(1|2)[0-9]|3[0-1])|(02)\-(0[1-9]|(1[0-9]|2[0-8])))$/gm.test(fecha)
    //    && 
    //}

    // obtener el fomulario del DOM por el ID
    //let donationForm = document.getElementById("add-donation");
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

    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");

    let isValid = true;
    //let msg = "";
    let InvalidInputs = [];


    const setInvalidInput = (inputName) =>{
        InvalidInputs.push(inputName);
        isValid&&=false;
    }

    if (!validarExiste(regioninput.value)) {
        setInvalidInput("Region");
    }

    if (!validarExiste(comunainput.value)) {
        setInvalidInput("Comuna");
    }

    if (!validarExiste(calleinput.value)) {
        setInvalidInput("Calle y Número");
    }

    if (!validarExiste(tipoinput.value)) {
        setInvalidInput("Tipo donación");
    }

    if (!validarExiste(cantidadinput.value)) {
        setInvalidInput("Cantidad");
    }

    if (!validarExiste(fechainput.value)) {
        setInvalidInput("Fecha");
    }

    if (!validarFotos(fotoinput.files)) {
        setInvalidInput("Fotos");
    } 

    if (!validarNombre(nombreinput.value)) {
        //msg += "El largo del nombre debe ser entre 2 y 80 caracteres\n";
        setInvalidInput("Nombre");
    } 

    if (!validarEmail(emailinput.value)) {
            //msg += "Email Incorrecto\n";
            setInvalidInput("Email");
    }

    if (!validarTelefono(celularinput.value)) {
            //msg += "Telefono Incorrecto\n";
            setInvalidInput("celular");
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
        if (confirm("¿Confirma que desea agregar esta donación?")){
            //donationForm.submit();
            alert("Hemos recibido la informacion de su donación. Muchas gracias.");
            //window.location.href = "../html/inicio.html";
        }
    }
};

const add_photo_fun=()=>{
    let photos_gather=document.getElementById("photos-gather");
    let add_photo_but=document.getElementById("add-photo");
    
    if(photos>=3){
        return ;
    }
    
    photos+=1;
    
    let input_id= "foto-donacion-"+toString(photos);

    let photo_div =document.createElement("div");
    photo_div.class="input-group mb-3";
    
    let photo_label=document.createElement("label");
    photo_label.class="input-group-text"
    photo_label.for=input_id
    photo_label.innerText="Foto donación";

    let photo_input=document.createElement("input");
    photo_input.class="form-control";
    photo_input.id=input_id;
    photo_input.name=input_id;
    photo_input.type="file";
    photo_input.multiple=true;
    photo_input.accept="image/*,.pdf";
    
    photo_div.append(photo_label);
    photo_div.append(photo_input);

    photos_gather.append(photo_div);

    if(photos>2){
        add_photo_but.hidden=true;
    }
}
// pip freeze > requirements.txt
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);

let add_photo = document.getElwmwnrById("add-photo");
add_photo.addEventListener("click", add_photo_fun)
