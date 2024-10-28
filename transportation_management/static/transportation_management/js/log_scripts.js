let allLogs = []; // Variable para almacenar todos los logs

// Función para cargar todos los logs al inicio
function loadAllLogs() {
    fetch('/api/logs/')
        .then(response => response.json())
        .then(data => {
            allLogs = data; // Almacena los logs obtenidos en la variable global
            filterLogs(); // Muestra los logs al cargar por primera vez
        })
        .catch(error => console.error("Error:", error));
}

// Función para filtrar y mostrar los logs según la placa ingresada
function filterLogs() {
    const searchPlate = document.getElementById("search_plate").value.toLowerCase();
    const filteredLogs = allLogs.filter(log => 
        log.vehicle_license_plate.toLowerCase().includes(searchPlate)
    );

    const logTableBody = document.getElementById("logTableBody");
    logTableBody.innerHTML = ""; // Limpia la tabla

    filteredLogs.forEach(log => {
        logTableBody.innerHTML += `
            <tr>
                <td>${log.vehicle_license_plate}</td>
                <td>${log.route_name}</td>
                <td>${log.assignment_date}</td>
            </tr>
        `;
    });
}

// Carga inicial sin filtros
loadAllLogs();
