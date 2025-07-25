'''
###################### AUN NO ESTA FUNCIONAL ######################
'''

import socket
import threading

# 5. El cliente crea su propio socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
host = '127.0.0.1'
port = 8080
client_socket.connect((host, port))
print('CONECTADO AL SERVIDOR')
print('[FROM SERVER] Envia "salir" para desconerctarte.')

# El cliente tendra hilos para
## 1) Enviar mensajes al servidor (lo que el usuario va a escribri)
def enviar_mensaje(cliente_socket):
    while True:
        try:
            mensaje = input()
        except EOFError:
            print("[ERROR] Se cerro la entrada.")
            break

        ## pedir al usuario que escriba algo y enviar eso al servidor
        if mensaje != '':
            print(f'[<<] ME: {mensaje}')
            cliente_socket.send(mensaje.encode('utf-8'))     # formato de transformacion unicode de 8 bits
        else:
            print('[i] El mensaje enviado por el cliente esta vacio')

        ## Si el mensaje es salir
            ## cerrar socket
        if mensaje == 'salir':
            print('[BYE] Cerrando conexion...')
            cliente_socket.close()
            break

## 2) Recibir mensajes desde el servidor
def recibir_mensaje(cliente_socket, nickname):
    ## estar siempre escuchando
    while True:
        try:
            response = cliente_socket.recv(2048).decode('utf-8')
            if response:
                print(f"\r{response}\n>> ", end="", flush=True)
                ## mostrar los mensajes recibidos del servidor
                print(f'[>>] {nickname}: {response}')
            else:
                print('[BYE] Cerrando conexion')
                cliente_socket.close()
                break
        except (ConnectionError, OSError):
            print('[ERROR] Se perdio la conexion con el servidor')
            cliente_socket.close()
            break

def comunicacion_con_server(cliente_socket):

    username = input("Ingresa un username: ")

    if username != '':
        cliente_socket.sendall(username.encode('utf-8'))
    else:
        print('El username no puede estar vacio')
        exit(0)

    # Hilos 
    thread_envio = threading.Thread(target=enviar_mensaje,args=(cliente_socket,))
    thread_recepcion = threading.Thread(target=recibir_mensaje, args=(cliente_socket,username))
    thread_envio.start()
    thread_recepcion.start() 

comunicacion_con_server(client_socket)
