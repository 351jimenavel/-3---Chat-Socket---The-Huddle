'''
2. Servidor multicliente con threads
Igual que el anterior, pero soportando varios clientes usando threading.
'''

#### Luego de completar la parte del servidor, empiezan los cambios en ese archivo

import socket
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
host = '127.0.0.1'
port = 8080
client_socket.connect((host, port))

# El cliente tendra hilos para
## 1) Enviar mensajes al servidor (lo que el usuario va a escribri)
    ## Opcion para salir del chat con comando o escribiendo "salir"
    ## Mientras no se haya escrito esto: pedir al usuario que escriba algo y enviar eso al servidor
    ## Si el mensaje es salir
        ## cerrar socket
        ## terminar hilo

## 2) Recibir mensajes desde el servidor
    ## estar siempre escuchando
    ## mostrar los mensajes recibidos del servidor