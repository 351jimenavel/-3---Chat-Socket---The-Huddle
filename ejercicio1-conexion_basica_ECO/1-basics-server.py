

# Importar la libreria socket para poder utilizarlo
import socket

## DESDE EL SERVIDOR
# 1. El servidor crea su socket propio
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. El servidor vincula su socket a la direccion IP y puerto que desea (localhost)
host = '127.0.0.1'
port = 8080
socket_server.bind((host, port))
# 3. El servidor escucha, osea espera por conexiones

print('Servidor activo....')
socket_server.listen()

# 4. El servidor acepta conexiones
#### cliente es un nuevo socket, independiente del socket que esta escuchando, que se utilizara para recibir y enviar data
#### address es una tupla (IP, puerto) del cliente que se conecto
cliente, address = socket_server.accept()
# 8. El servidor recibe data (mensaje) por parte del cliente
mensaje = cliente.recv(2048).decode('utf-8')
print('Mensaje recibido del cleinte:', mensaje)
# 9. El servidor envia data al cliente
cliente.send(mensaje.encode())
# 12. El servidor recibe el mensaje de cierre del cliente
mensaje_cierre = cliente.recv(2048).decode('utf-8')
print('Ok, cerrando cliente...')
cliente.close()
# 13. El servidor cierra su conexion
print('Cerrando server...')
socket_server.close()

## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
# 7. El cliente envia data (mensaje) 
# 10. El cliente recibe data del servidor
# 11. El cliente decide cerrar conexion