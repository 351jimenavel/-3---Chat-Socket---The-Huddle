'''
2. Servidor multicliente con threads
Igual que el anterior, pero soportando varios clientes usando threading.
'''
import socket
import threading        # threading ayuda implementar concurrencia a traves de hilos. Permite ejecutar multiples tareas simultaneamente dentro de un mismo programa.

## OBjetivo: Crear una estructura concurrente, donde cada cliente sea atendido por su propio hilo

## La estructura es la misma que la anterior con variaciones (Estas variaciones seran identificadas asi: (*))
# Se crea el socket del servidor
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
socket_server.bind((host, port))

print('Servidor activo....')
socket_server.listen()

lista_de_clientes = []

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
        
# (*) Aca ya no solo tiene que ser aceptar una sola conexion sino infinitas
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