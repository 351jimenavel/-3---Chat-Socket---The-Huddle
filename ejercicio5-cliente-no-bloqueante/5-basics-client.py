'''5. Cliente no bloqueante: 
Que pueda leer del usuario y del socket sin bloquearse. 
Usa select.select([stdin,socket],...) o threads ligeros'''

### ! Objetivo: Crear un cliente que pueda leer del teclado y del servidor al mismo tiempo sin usar threads.

## Estructura para el cliente

# 1. importar lo necesario
### socket (crear socket del cliente)
import socket
### select (esperar multiples eventos a la vez)
import select
### sys (leer del taclado 'stdin')
import sys

# 2. Crear socket del cliente
host = '127.0.0.1'
port = 23456
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# 3. Loop principal
while True:
### 3.1 Tendra la tarea de:
### (a) escuchar lo que escribe el usuario
### (b) escuchar lo que llega del servidor
####### al mismo tiempo!!!
    lectura, _, _ = select.select([sys.stdin, client_socket], [], [])
    for fuente in lectura:
        ### 3.2 si hay datos en stdin
        if fuente == sys.stdin:
            ### leer lo que el usuario escribrio
            mensaje = sys.stdin.readline().strip()
            ### si el mensaje es salir, cerrar todo
            if mensaje.lower() == 'salir':
                print('Cerrando conexion...')
                client_socket.close()
                sys.exit()
            ### si el mensaje no esta vacio, mandar al servidor
            if mensaje != '':
                client_socket.send(mensaje.encode('utf-8'))
            
        ### 3.3 si hay datos en socket
        elif fuente == client_socket:
            ### leer el mensaje que llego desde el servidor
            data = client_socket.recv(2048).decode('utf-8')
            ### si el mensaje esta vacio, cerrar todo
            if not data:
                print("Servidor cerro la conexion")
                client_socket.close()
                sys.exit()
            ### mostrar mensaje si es que hay
            print(f'Servidor dice: {data}')