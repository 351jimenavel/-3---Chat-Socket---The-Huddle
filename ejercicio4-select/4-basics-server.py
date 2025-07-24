'''4. Servidor sin threads usando select
Usá una lista de sockets y select.select() para aceptar y leer múltiples clientes sin usar hilos.'''

## ! Objetivo: manejar múltiples clientes al mismo tiempo reemplazando threading por select.select()
# select.select() permite monitorear varios sockets a la vez y saber cuáles están listos para leer/escribir.
## Modulo select --> esperando finalizacion de input/output

# Estructura del servidor

# 1. Crear el socket del servidor
    # socket
    # bind
    # listen

# 2. Crear una lista de sockets activos (socket del servidor incluido)
# 3. Flujo del servidor
    # Mantener el servidor corriendo
    # usar select para detectar actividad (leer, escribir, errores)
# 4. Manejar eventos en los sockets
    # utilizar el dato de leer de select
        # aceptar nueva conexion (si el socket es el del servidor)
            # agregar la conexion a la lista de sockets activos
        # si el socket es del cliente
            # intentar leer datos
                # si se reciben datos
                    # procesarlos o hacer broadcast
                # si no, mostrar cliente desconectado
                    # cerrar
                    # quitarlo de la lista
# 5. Si un cliente se va, eliminar su socket de la lista y cerrar conexion