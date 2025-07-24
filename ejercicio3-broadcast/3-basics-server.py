'''3. Broadcast manual
Al recibir un mensaje de un cliente, el server lo reenvía a todos los demás.'''

import socket
import threading        # threading ayuda implementar concurrencia a traves de hilos. Permite ejecutar multiples tareas simultaneamente dentro de un mismo programa.

## ! Objetivo: Cuando el servidor recibe un mensaje de un cliente, lo reenvia a todos los clientes conectados (BROADCAST)

# Se crea el socket del servidor
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
socket_server.bind((host, port))

print('Servidor activo....')
socket_server.listen()

lista_de_clientes = []

'''En la version anterior el servidor actuaba como un receptor nada mas haciendo:
            print(f'{cliente_socket}:{addr} ha enviado el siguiente mensaje: {mensaje}')'''
            # Ahora tiene que:
            # Difundir mensaje a todos los clientes (BROADCAST)
                # DETALLE: que solo les aparezca a los demas clientes, no a uno mismo
                # mostrar mensaje
                # Practicar manejo de errores (EJ: eliminar al cliente de la lista si se cierra conexion, verificar que este en la lista, etc)

#### Funcion manejar cliente:
def handle_clients(cliente_socket, addr):
    connected = True
# Mientras el cliente este conectado
    while connected:
        ## Escuchar los mensajes que envia
        mensaje = cliente_socket.recv(2048).decode('utf-8')
        if mensaje != '':
            print(f'{cliente_socket}:{addr} ha enviado el siguiente mensaje: {mensaje}')

        ## Si el mensaje es 'salir', cortar conexion y salir del hilo
        if mensaje == 'salir':
            print(f'Cerrando conexion de {cliente_socket}:{addr}')
            cliente_socket.close()
            connected = False       # para romper el loop

## Mientras el servidor este corriendo:
while True:
    ### Aceptar una nueva conexion (cliente y direccion)
    cliente, address = socket_server.accept()
    ### Crear un hilo nuevo que se encargue de ese cliente
    thread_clients = threading.Thread(target=handle_clients, args=(cliente, address))
    thread_clients.start()
    ### El hilo tendra la tarea de ejercutar una funcion que maneje solo a ese cliente.

    #### Llevar registro de todos los clientes conectados 
    lista_de_clientes.append(cliente)
