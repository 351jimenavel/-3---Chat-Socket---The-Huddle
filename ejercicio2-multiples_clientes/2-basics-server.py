'''
2. Servidor multicliente con threads
Igual que el anterior, pero soportando varios clientes usando threading.
'''
import socket
import threading        # threading ayuda implementar concurrencia a traves de hilos. Permite ejecutar multiples tareas simultaneamente dentro de un mismo programa.

## OBjetivo: Crear una estructura concurrente, donde cada cliente sea atendido por su propio hilo

