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
