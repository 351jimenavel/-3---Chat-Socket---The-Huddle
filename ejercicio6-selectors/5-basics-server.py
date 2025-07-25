'''Crear un servidor eco no bloqueante que:

Acepte múltiples clientes.

Use selectors para manejar conexiones (en vez de threads o select.select).

Devuelva a cada cliente lo que le envía (modo eco).

Permanezca activo sin trabarse mientras espera mensajes.'''

## La resolucion de la consigna se hara en este archivo

#############################################################################################################
#                                                                                                           #
#       ---> Que es 'selectors'?                                                                            #
#                                                                                                           #
#       Es un modulo de Python que permite registrar sockets para 'monitorear' si:                          #
#           (a) estan listos para leer                                                                      #
#           (b) estan listos para escribir                                                                  #
#           (c) se cerraron o lanzaron un error                                                             #    
#      Todo esto lo hace de manera eficiente y viene genial para una estructura de                          #
#      muchos clientes conectados al mismo tiempo                                                           #
#                                                                                                           #
#      ---> selects vs selectors                                                                            #
#                                                                                                           #
#      1. Select requiere que se le pasen listas manualmente para verificar cuales sockets estan listos     #
#         Tiene limitaciones (esp. en windows) y puede resultar incomodo si el programa crece               #
#      2. Selectors permite registrar sockets junto con el evento que querés manejar                        #
#         (como lectura o escritura), y luego te avisa cuáles están listos, haciendo el código              #
#         más limpio, escalable y fácil de mantener.                                                        #
#                                                                                                           #
#############################################################################################################

## ESTRUCTURA DEL SERVER

import socket
import selectors

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Configurar el socket
### bind
host = '127.0.0.1'
port = 34567
server_socket.bind((host,port))
server_socket.listen()
print(f'Server en modo escucha desde {(host, port)}')
### setear como no bloqueante
server_socket.setblocking(False)
# Crear un selector
sel = selectors.DefaultSelector()

# Registrar el socket del servidor en el selector
sel.register(server_socket, selectors.EVENT_READ, data=None)
### evento: event_read para saber cuando llega una nueva conexion

# Loop principal
try:
    while True:
        ### llamar a selector.select() para ver que socket esta listo
        eventos = sel.select(timeout=None)
        ### Por cada socket listo:
        for event in eventos:
            # (a) Si el socket es del servidor (llega nueva conexion):
            if event.fileobj is server_socket:
                # aceptar la conexion
                nueva_conn, addr = server_socket.accept()
                # hacerla no bloqueante
                nueva_conn.setblocking(False)
                # registrar ese nuevo socket en el selector
                sel.register(nueva_conn, selectors.EVENT_READ, data=None)
                    # evento: event_read (esperar datos del cliente)
                    
            # (b) Si es un socket de cliente (mandó datos):
            else:
                sock = event.fileobj    # socket del cliente que esta listo
                try:
                # leer los datos
                    mensaje = sock.recv(2048).decode('utf-8')
                    # si mandó algo:
                    if mensaje:
                        # procesar e imprimir
                        print(f'Mensaje recibido: {mensaje}')
                        # enviar de nuevo (ECO)
                        sock.send(mensaje.encode())
                    else:
                    # si no (desconexión):
                        print("Cliente desconectado")
                        # cerrar el socket y removerlo del select
                        sel.unregister(sock)
                        sock.close()
                except ConnectionError:
                    print("Error de conexion con cliente")
                    sel.unregister(sock)
                    sock.close()
                    
except KeyboardInterrupt:
    print('Interrupcion manual, cerrando servidor...')
finally:
    sel.close()