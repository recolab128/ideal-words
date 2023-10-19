// validacion.js

function validarFormulario() {
    let opciones_sugeridas = document.getElementById("opcionesUsuario").value;
    if (opciones_sugeridas.length !== 0) {
        const regex = /^([a-zA-ZáéíóúÁÉÍÓÚüÜ0-9]+[, ]?)*[a-zA-ZáéíóúÁÉÍÓÚüÜ0-9]+$/;
        resultado = regex.test(opciones_sugeridas)
        if (!resultado) {
            let contenedorErrores = document.getElementById("errores");
            if (!contenedorErrores.firstChild) {
                let nodoTexto = document.createTextNode("Error: Formato Inadecuado. Solo se permiten palabras separadas por comas.");
                contenedorErrores.appendChild(nodoTexto);
            }
        }
    }
    return resultado

}

// function validarCadena(sugerencias) {
// var regex = /^\s*[\w\s]+(?:,\s*[\w\s]+)*\s*$/;
//    return regex.test(sugerencias)
// }