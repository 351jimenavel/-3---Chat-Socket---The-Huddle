'''4. Servidor sin threads usando select
Usá una lista de sockets y select.select() para aceptar y leer múltiples clientes sin usar hilos.'''

## ! Objetivo: manejar múltiples clientes al mismo tiempo reemplazando threading por select.select()
# select.select() permite monitorear varios sockets a la vez y saber cuáles están listos para leer/escribir.
## Modulo select --> esperando finalizacion de input/output

# Estructura del servidor

import socket
import select
## 1. Crear el socket del servidor
# socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind
host = '127.0.0.1'
port = 5555
server_socket.bind((host, port))
# listen
server_socket.listen()

# 2. Crear una lista de sockets activos (socket del servidor incluido)
lista_sockets_activos = [server_socket]

# 3. Flujo del servidor
while True:
    # Mantener el servidor corriendo
    # usar select para detectar actividad (leer, escribir, errores)
    #### el importante por el momento es el de leer, ya que necesito saber cuales son los sockets que tienen algo para leer
    sockets_lectura, _,_ = select.select(lista_sockets_activos, [], [])

# 4. Manejar eventos en los sockets
    # iterar sobre el dato de leer de select
    for socket_actual in sockets_lectura:
        # aceptar nueva conexion (si el socket es el del servidor)
        if socket_actual == server_socket:
            nuevo_cliente, addr = server_socket.accept()
            # agregar la conexion a la lista de sockets activos
            lista_sockets_activos.append(nuevo_cliente)
        # si el socket es del cliente
        else:
            # intentar leer datos
            try:
                mensaje = socket_actual.recv(2048).decode('utf-8')
                # si se reciben datos
                if mensaje:
                    # procesarlos o hacer broadcast
                    print(f'{addr} ha enviado: {mensaje}')
                    for cliente in lista_sockets_activos:
                        if cliente != socket_actual and cliente != server_socket:
                            try:
                                cliente.send(f'{addr}:{mensaje}'.encode())
                            except ConnectionResetError:
                                print(f'Error al enviar mensaje a {cliente}, eliminando')
                                try:
                                    lista_sockets_activos.remove((cliente,addr))
                                except ValueError:
                                    pass
                # si no, mostrar cliente desconectado
                else:
                    print(f'Error en {addr}, desconectando cliente...')
                    # cerrar
                    # quitarlo de la lista
                    try:
                        lista_sockets_activos.remove((nuevo_cliente, addr))
                    except ValueError:
                        pass
                    socket_actual.close()

# 5. Si un cliente se va, eliminar su socket de la lista y cerrar conexion
            except ConnectionResetError:
                print(f'{addr} se desconecto inesperadamente')
                try:
                    lista_sockets_activos.remove((nuevo_cliente, addr))
                except ValueError:
                    pass
                socket_actual.close()