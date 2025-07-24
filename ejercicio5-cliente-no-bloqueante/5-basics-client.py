'''5. Cliente no bloqueante: 
Que pueda leer del usuario y del socket sin bloquearse. 
Usa select.select([stdin,socket],...) o threads ligeros'''

### ! Objetivo: Crear un cliente que pueda leer del teclado y del servidor al mismo tiempo sin usar threads.

## Estructura para el cliente

# 1. importar lo necesario
### socket (crear socket del cliente)
### select (esperar multiples eventos a la vez)
### sys (leer del taclado 'stdin')

# 2. Crear socket del cliente

# 3. Loop principal
### 3.1 Tendra la tarea de:
### (a) escuchar lo que escribe el usuario
### (b) escuchar lo que llega del servidor
####### al mismo tiempo!!!

### 3.2 si hay datos en stdin
### leer lo que el usuario escribrio
### si el mensaje no esta vacio, mandar al servidor
### si el mensaje es salir, cerrar todo

### 3.3 si hay datos en socket
### leer el mensaje que llego desde el servidor
### mostrarlo
### si el mensaje esta vacio, cerrar todo