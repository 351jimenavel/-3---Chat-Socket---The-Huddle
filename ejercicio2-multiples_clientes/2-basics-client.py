'''
2. Servidor multicliente con threads
Igual que el anterior, pero soportando varios clientes usando threading.
'''

#### Aun no se realizaron cambios aca

# Importar la libreria socket para poder utilizarlo

## DESDE EL SERVIDOR
# 1. El servidor crea su socket propio
# 2. El servidor vincula su socket a la direccion IP y puerto que desea (localhost)
# 3. El servidor escucha, osea espera por conexiones
# 4. El servidor acepta conexiones
# 8. El servidor recibe data (mensaje) por parte del cliente
# 9. El servidor envia data al cliente
# 12. El servidor recibe el mensaje de cierre del cliente
# 13. El servidor cierra su conexion
########################

import socket
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
host = '127.0.0.1'
port = 8080
client_socket.connect((host, port))
# 7. El cliente envia data (mensaje)
client_socket.send('Hola servidor'.encode('utf-8')) 
# 10. El cliente recibe data del servidor
response = client_socket.recv(2048).decode('utf-8')
print('Eco del servidor: ', response)
# 11. El cliente decide cerrar conexion
client_socket.send('Cierro conexion'.encode('utf-8'))
print('chau')
client_socket.close()