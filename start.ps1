$CONTAINER_NAME = "cont_django_app"
$IMAGE_NAME = "img_django_app"
$IMAGE_TAG = "latest"
$PORT_MAP = "8000:8000"

# Comprobar si el contenedor está corriendo y detenerlo
if (docker ps -q -f "name=^/$CONTAINER_NAME$") {
    Write-Output "El contenedor $CONTAINER_NAME está corriendo. Deteniéndolo..."
    docker stop $CONTAINER_NAME
    Write-Output "Contenedor detenido."
} else {
    Write-Output "El contenedor $CONTAINER_NAME no está corriendo."
}

# Comprobar si el contenedor existe y eliminarlo
if (docker ps -aq -f "name=^/$CONTAINER_NAME$") {
    Write-Output "El contenedor $CONTAINER_NAME existe. Eliminándolo..."
    docker rm $CONTAINER_NAME
    Write-Output "Contenedor eliminado."
}

# Comprobar si la imagen existe y eliminarla
if (docker images -q "${IMAGE_NAME}:${IMAGE_TAG}") {
    Write-Output "La imagen ${IMAGE_NAME}:${IMAGE_TAG} existe. Eliminándola..."
    docker rmi "${IMAGE_NAME}:${IMAGE_TAG}"
    Write-Output "Imagen eliminada."
}

# Construir la nueva imagen Docker
Write-Output "Construyendo la imagen Docker ${IMAGE_NAME}:${IMAGE_TAG}..."
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
Write-Output "Imagen construida."

# Ejecutar el contenedor
Write-Output "Ejecutando el contenedor..."
docker run -d -p $PORT_MAP --restart unless-stopped --name $CONTAINER_NAME -e NEO4J_URI="neo4j+s://neo4j:EKPkZ-JNRUQ_qYl4C3MspTIimc-a5Dvtc03bW-8H9rw@81995a9d.databases.neo4j.io" "${IMAGE_NAME}:${IMAGE_TAG}"
Write-Output "Contenedor $CONTAINER_NAME ejecutándose en background."

# Validar el estado del contenedor
Write-Output "Validando el estado del contenedor $CONTAINER_NAME, ESPERE..."
Start-Sleep -Seconds 5

if (docker ps -q -f "name=^/$CONTAINER_NAME$") {
    Write-Output "El contenedor $CONTAINER_NAME está corriendo normalmente. FIN SCRIPT."
} else {
    Write-Output "El contenedor $CONTAINER_NAME NO está corriendo. Verificar el problema."
}
