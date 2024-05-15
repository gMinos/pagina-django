// Obtener la fecha actual
function mostrarFechaActual() {
    var fechaActual = new Date();
    var dia = fechaActual.getDate();
    var mes = fechaActual.getMonth() + 1; // Los meses comienzan desde 0
    var año = fechaActual.getFullYear();

    // Formatear la fecha como "DD/MM/AAAA"
    var fechaFormateada = dia + '/' + mes + '/' + año;

    // Mostrar la fecha en el elemento con el id "fecha-actual"
    var elementoFecha = document.getElementById("fecha-actual");
    if (elementoFecha) {
        elementoFecha.textContent = fechaFormateada;
    }
}

console.log('hola mundo')

// Llamar a la función para mostrar la fecha actual cuando se cargue la página
mostrarFechaActual();
