'''3. Broadcast manual
Al recibir un mensaje de un cliente, el server lo reenvía a todos los demás.'''

#### Continua la version del ejercicio 2. 

import socket
import threading
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
host = '127.0.0.1'
port = 8080
client_socket.connect((host, port))
print('CONECTADO AL SERVIDOR')
# El cliente tendra hilos para
## 1) Enviar mensajes al servidor (lo que el usuario va a escribri)
def enviar_mensaje(cliente_socket):
    ## Opcion para salir del chat con comando o escribiendo "salir"
    while True:
        mensaje = input()
    ## Mientras no se haya escrito esto: pedir al usuario que escriba algo y enviar eso al servidor
        if mensaje != '':
            print('Mensaje enviado')
            client_socket.send(mensaje.encode())
        else:
            print('El mensaje enviado por el cliente esta vacio')
    ## Si el mensaje es salir
        ## cerrar socket
        ## terminar hilo
        if mensaje == 'salir':
            print('Cerrando conexion...')
            cliente_socket.close()
            break

## 2) Recibir mensajes desde el servidor
def recibir_mensaje(cliente_socket):
    ## estar siempre escuchando
    while True:
        try:
            response = client_socket.recv(2048).decode('utf-8')
            if response:
                ## mostrar los mensajes recibidos del servidor
                print(f'Mensaje recibido: {response}')
            else:
                print('Cerrando conexion...')
                cliente_socket.close()
                break
        except ConnectionError:
            print('Error de conexion')
            cliente_socket.close()
            break

thread_envio = threading.Thread(target=enviar_mensaje,args=(client_socket,))
thread_recepcion = threading.Thread(target=recibir_mensaje, args=(client_socket,))
thread_envio.start()
thread_recepcion.start() 