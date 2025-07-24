'''5. Cliente no bloqueante: 
Que pueda leer del usuario y del socket sin bloquearse. 
Usa select.select([stdin,socket],...) o threads ligeros'''

# Estructura del servidor igual a la del ejercicio 4-select

import socket
import select
## 1. Crear el socket del servidor
# socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind
host = '127.0.0.1'
port = 23456
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
                    print(f'Cliente ha enviado: {mensaje}')
                    for cliente in lista_sockets_activos:
                        if cliente != socket_actual and cliente != server_socket:
                            try:
                                cliente.send(mensaje.encode())
                            except:
                                print(f'Error al enviar mensaje')
                                cliente.close()
                                try:
                                    lista_sockets_activos.remove(cliente)
                                except ValueError:
                                    print('Ese cliente ya no estaba en la lista (probablemente se ha desconectado)')
                                    pass
                # si no, mostrar cliente desconectado
                else:
                    print(f'Cliente desconectado')
                    # cerrar
                    socket_actual.close()
                    # quitarlo de la lista
                    try:
                        lista_sockets_activos.remove(socket_actual)
                    except ValueError:
                        print('Ese cliente ya no estaba en la lista (probablemente se ha desconectado)')
                        pass

            # 5. Si un cliente se va, eliminar su socket de la lista y cerrar conexion
            except:
                print('Error con cliente')
                socket_actual.close()
                try:
                    lista_sockets_activos.remove(socket_actual)
                except ValueError:
                    print('Ese cliente ya no estaba en la lista (probablemente se ha desconectado)')
                    pass