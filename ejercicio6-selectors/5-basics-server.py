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

# Crear un socket del servidor

# Configurar el socket
### bind
### setear como no bloqueante

# Crear un selector

# Registrar el socket del servidor en el selector
### evento: event_read para saber cuando llega una nueva conexion

# Loop principal
### llamar a selector.select() para ver que socket esta listo
### Por cada socket listo:
    # (a) Si el socket es del servidor (llega nueva conexion):
        # aceptar la conexion
        # hacerla no bloqueante
        # registrar ese nuevo socket en el selector
            # evento: event_read (esperar datos del cliente)
    # (b) Si es un socket de cliente (mandó datos):
        # leer los datos
        # si mandó algo:
            # procesar e imprimir
            # enviar de nuevo (ECO)
        # si no (desconexión):
            # cerrar el socket y removerlo del select