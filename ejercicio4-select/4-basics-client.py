'''4. Servidor sin threads usando select
Usá una lista de sockets y select.select() para aceptar y leer múltiples clientes sin usar hilos.'''

'''Al ser el ejercicio directamente para reemplazar threads en el lado del servidor, el archivo cliente se mantiene como en el ejercicio 3-Broadcast'''

import socket
import threading
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
host = '127.0.0.1'
port = 5555     # Se agrega un puerto diferente ya que en el socket del servidor se utiliza este
client_socket.connect((host, port))
print('CONECTADO AL SERVIDOR')

# El cliente tendra hilos para
## 1) Enviar mensajes al servidor (lo que el usuario va a escribri)
def enviar_mensaje(cliente_socket):
    ## Opcion para salir del chat con comando o escribiendo "salir"
    while True:
        try:
            mensaje = input()
        except EOFError:
            print("Se cerro la entrada.")
            break
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
        except (ConnectionError, OSError):
            print('Se perdio la conexion con el servidor')
            cliente_socket.close()
            break

thread_envio = threading.Thread(target=enviar_mensaje,args=(client_socket,))
thread_recepcion = threading.Thread(target=recibir_mensaje, args=(client_socket,))
thread_envio.start()
thread_recepcion.start() 