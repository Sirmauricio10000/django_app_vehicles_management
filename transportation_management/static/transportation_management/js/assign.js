document.addEventListener("DOMContentLoaded", function () {
    try {
        const vehiclesData = document.getElementById("vehicles-data").textContent.trim();
        const routesData = document.getElementById("routes-data").textContent.trim();
        
        window.vehicles = JSON.parse(vehiclesData);
        window.routes = JSON.parse(routesData);

        populateSelectOptions("vehicle", window.vehicles, "id", "license_plate", "vehicle_type");
        populateSelectOptions("route", window.routes, "id", "name", "route_type");

        updateVehicleDetails();

    } catch (e) {
        console.error("Error parsing JSON data:", e);
    }
});

function populateSelectOptions(selectId, data, valueField, displayField1, displayField2) {
    const selectElement = document.getElementById(selectId);
    
    data.forEach(item => {
        const option = document.createElement("option");
        option.value = item[valueField];
        option.textContent = `${item[displayField1]} - ${item[displayField2]}`;
        selectElement.appendChild(option);
    });
}

function updateVehicleDetails() {
    const vehicleId = document.getElementById("vehicle").value;
    const vehicle = window.vehicles.find(v => String(v.id) === String(vehicleId));

    // Si se encuentra el vehículo, muestra sus detalles
    if (vehicle) {
        document.getElementById("vehiclePlate").textContent = vehicle.license_plate;
        document.getElementById("vehicleType").textContent = vehicle.vehicle_type;
        document.getElementById("vehicleStatus").textContent = vehicle.status;
        document.getElementById("vehicleAssignedRoute").textContent = vehicle.route_id ? "Yes" : "No";
    } else {
        // Si no hay ningún vehículo seleccionado, limpia los campos
        document.getElementById("vehiclePlate").textContent = "-";
        document.getElementById("vehicleType").textContent = "-";
        document.getElementById("vehicleStatus").textContent = "-";
        document.getElementById("vehicleAssignedRoute").textContent = "-";
    }
}

function updateRouteDetails() {
    const routeId = document.getElementById("route").value;
    const route = window.routes.find(r => String(r.id) === String(routeId));

    document.getElementById("routeName").textContent = route ? route.name : "-";
    document.getElementById("routeOrigin").textContent = route ? route.origin : "-";
    document.getElementById("routeDestination").textContent = route ? route.destination : "-";
    document.getElementById("routeDistance").textContent = route ? route.distance : "-";
    document.getElementById("routeType").textContent = route ? route.route_type : "-";
}

function refreshVehicleData(vehicleId) {
    fetch(`/api/vehicles/${vehicleId}/`)
        .then(response => response.json())
        .then(data => {
            // Encuentra el vehículo en la lista y actualiza sus datos
            const index = window.vehicles.findIndex(v => v.id === data.id);
            if (index !== -1) {
                window.vehicles[index] = data;
            }

            // Actualiza los detalles en la tabla
            updateVehicleDetails();
        })
        .catch(error => {
            console.error("Error fetching updated vehicle data:", error);
        });
}

function assignVehicle() {
    const vehicleId = document.getElementById("vehicle").value;
    const routeId = document.getElementById("route").value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if (!vehicleId || !routeId) {
        showMessage("Please select both a vehicle and a route.", false);
        return;
    }

    fetch(`/api/vehicles/${vehicleId}/`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ "route_id": routeId })
    })
    .then(response => {
        return response.json().then(data => ({ status: response.status, data }));
    })
    .then(({ status, data }) => {
        if (status === 400 || data.error) {
            showMessage(data.error || "Failed to assign vehicle.", false);
        } else {
            showMessage("Vehicle assigned successfully.", true);
            refreshVehicleData(vehicleId); // Refresca los datos del vehículo después de asignar
        }
    })
    .catch(error => {
        console.error("Error:", error);
        showMessage("An error occurred. Please try again.", false);
    });
}

function unassignRoute() {
    const vehicleId = document.getElementById("vehicle").value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if (!vehicleId) {
        showMessage("Please select a vehicle to unassign.", false);
        return;
    }

    fetch(`/api/vehicles/${vehicleId}/`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ "route_id": null })
    })
    .then(response => {
        return response.json().then(data => ({ status: response.status, data }));
    })
    .then(({ status, data }) => {
        if (status === 400 || data.error) {
            showMessage(data.error || "Failed to unassign route.", false);
        } else {
            showMessage("Route unassigned successfully.", true);
            refreshVehicleData(vehicleId); // Refresca los datos del vehículo después de desasignar
        }
    })
    .catch(error => {
        console.error("Error:", error);
        showMessage("An error occurred. Please try again.", false);
    });
}

function showMessage(message, isSuccess) {
    const resultMessage = document.getElementById("resultMessage");
    resultMessage.innerHTML = message;
    resultMessage.className = isSuccess ? "success" : "error"; // Aplica clase de estilo
}

document.getElementById("vehicle").addEventListener("change", updateVehicleDetails);
document.getElementById("route").addEventListener("change", updateRouteDetails);
