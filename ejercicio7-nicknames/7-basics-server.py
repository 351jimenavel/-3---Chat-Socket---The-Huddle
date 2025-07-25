'''
###################### AUN NO ESTA FUNCIONAL ######################
'''

import socket
import threading        
# threading ayuda implementar concurrencia a traves de hilos. Permite ejecutar multiples tareas simultaneamente dentro de un mismo programa.


# Se crea el socket del servidor
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
socket_server.bind((host, port))

socket_server.listen()
print("---[SERVIDOR ACTIVO]---")
print(" ¡Esperando conexiones! ")

lista_de_clientes = []      # tendra socket : username
            
def broadcast(mensaje, cliente_emisor):
    # Difundir mensaje a todos los clientes (BROADCAST)
    for cliente, user in lista_de_clientes:
        if cliente != cliente_emisor:
            # mostrar mensaje
            try:
                cliente.send(mensaje.encode())
            except ConnectionResetError:
                print(f'[DESCONECTADO] {user} fue eliminando')
                cliente.close()
                # antes de eliminar cliente, verificar si esta en la lista
                try:
                    lista_de_clientes.remove((cliente,user))
                except ValueError:
                    pass
                print(f'[i] Total de clientes conectados: {len(lista_de_clientes)}')

#### Funcion manejar cliente:
def handle_clients(cliente_socket):
    try:
        username = cliente_socket.recv(2048).decode('utf-8')

        if not username:
            cliente_socket.close()
            return

        lista_de_clientes.append((cliente_socket, username))
        print(f'[+] {username} se ha conectado')
        broadcast(f'[{username}] se ha unido al chat.', cliente_socket)

        connected = True
        # Mientras el cliente este conectado
        while connected:
            try:
                ## Escuchar los mensajes que envia
                mensaje = cliente_socket.recv(2048).decode('utf-8')
                if mensaje != '':
                    print(f'[NEW MESSAGE] {username} : {mensaje}')
                    broadcast(f'[{username}] {mensaje}', cliente_socket)

                ## Si el mensaje es 'salir', cortar conexion y salir del hilo
                if mensaje.lower() == 'salir':
                    print(f'[!] {username} se ha desconectado')
                    broadcast(f'[{username}] ha salido del chat', cliente_socket)
                    cliente_socket.close()
                    try:
                        lista_de_clientes.remove((cliente_socket, username))
                    except ValueError:
                        print('[!] Ese cliente ya no estaba en la lista (probablemente se ha desconectado)')
                    connected = False       # para romper el loop
                    print(f'[i] Total de clientes conectados: {len(lista_de_clientes)}')
            
            except (ConnectionResetError, KeyboardInterrupt, EOFError):
                print(f'[!] {username} se desconecto inesperadamente')
                try:
                    lista_de_clientes.remove((cliente_socket, username))
                except ValueError:
                    pass
                cliente_socket.close()
                print(f'[i] Total de clientes conectados: {len(lista_de_clientes)}')
                broadcast(f'[{username}] se ha desconectado.', cliente_socket)
                connected = False

    except Exception as e:
        print(f'[ERROR] Fallo la conexion inicial con un cliente: {e}')
        cliente_socket.close()
        

## Mientras el servidor este corriendo:
while True:
    ### Aceptar una nueva conexion (cliente y direccion)
    cliente, address = socket_server.accept()
    print(f'[NEW CONNECTION ESTABLISHED] {address}')
    print(f'[i] Total de clientes conectados: {len(lista_de_clientes)+1}')

    ### Crear un hilo nuevo que se encargue de ese cliente
    ### El hilo tendra la tarea de ejercutar una funcion que maneje solo a ese cliente.
    thread_clients = threading.Thread(target=handle_clients, args=(cliente, ))
    thread_clients.start()

    #### Llevar registro de todos los clientes conectados 
    #lista_de_clientes.append((cliente, address))
