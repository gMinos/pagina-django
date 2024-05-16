document.addEventListener('DOMContentLoaded', function() {
    // Obtener el elemento donde se mostrará la fecha y hora
    const fechaElemento = document.getElementById('fecha');

    // Función para actualizar la fecha y hora
    function actualizarFechaHora() {
        // Obtener la fecha y hora actual
        const fechaActual = new Date();

        // Formatear la fecha
        const dia = fechaActual.getDate();
        const mes = fechaActual.getMonth() + 1;
        const anio = fechaActual.getFullYear();

        // Formatear la hora
        let horas = fechaActual.getHours();
        const minutos = fechaActual.getMinutes();
        const segundos = fechaActual.getSeconds();

        // Ajustar el formato de las horas si es necesario
        if (horas < 10) {
            horas = '0' + horas;
        }

        // Mostrar la fecha y hora en el elemento
        fechaElemento.textContent = dia + '/' + mes + '/' + anio + ' ' + horas + ':' + minutos + ':' + segundos;
    }

    // Llamar a la función inicialmente para mostrar la fecha y hora actual
    actualizarFechaHora();

    // Actualizar la fecha y hora cada segundo
    setInterval(actualizarFechaHora, 1000);
});
