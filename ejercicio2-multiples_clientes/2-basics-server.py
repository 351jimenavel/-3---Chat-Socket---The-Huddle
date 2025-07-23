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

#
cliente, address = socket_server.accept()

mensaje = cliente.recv(2048).decode('utf-8')
print('Mensaje recibido del cleinte:', mensaje)

cliente.send(mensaje.encode())

mensaje_cierre = cliente.recv(2048).decode('utf-8')
print('Ok, cerrando cliente...')
cliente.close()

print('Cerrando server...')
socket_server.close()

################################
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
# 7. El cliente envia data (mensaje) 
# 10. El cliente recibe data del servidor
# 11. El cliente decide cerrar conexion