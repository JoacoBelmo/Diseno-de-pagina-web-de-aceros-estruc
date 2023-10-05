// Cargar el archivo JSON con los datos
fetch('datos.json')
    .then(response => response.json())
    .then(data => {
        const formulario = document.getElementById('formulario');
        const resultado = document.getElementById('resultado');

        function mostrarInformacion() {
            // Obtener el valor del input con el índice
            const indiceInput = document.getElementById('indice');
            const indice = parseInt(indiceInput.value);
        
            // Verificar si el índice es válido
            if (!isNaN(indice) && indice >= 0 && indice < data.length) {
                // Obtener la información asociada al índice
                const informacion = data[indice];
        
                // Crear una lista de elementos para mostrar la información
                const lista = document.createElement('ul');
                for (const key in informacion) {
                    // Verificar si la propiedad existe y no es null antes de mostrarla
                    if (informacion.hasOwnProperty(key) && informacion[key] !== null) {
                        const listItem = document.createElement('li');
                        // Mostrar la propiedad y su valor en un elemento de lista
                        listItem.textContent = `${key}: ${informacion[key]}`;
                        lista.appendChild(listItem);
                    }
                }
                // Limpiar el resultado anterior y mostrar la nueva lista
                resultado.innerHTML = '';
                resultado.appendChild(lista);
            } else {
                // Mostrar un mensaje de error si el índice no es válido
                resultado.innerHTML = 'Índice no válido.';
            }
        }
        
        // Agregar un evento al formulario para llamar a la función mostrarInformacion() cuando se envía
        formulario.addEventListener('submit', function (e) {
            e.preventDefault();
            mostrarInformacion();
        });
    }
);