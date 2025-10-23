# 🛰️ Challenge 4 – Chat en tiempo real con Sockets  
**The Huddle – Penguin Academy**

Autora: Jimena Velázquez

---

## 🇪🇸 Español

### 📖 Descripción  
Este proyecto implementa una **aplicación de chat en tiempo real** desarrollada desde cero utilizando **sockets TCP** en Python.  
El objetivo fue **reconstruir la comunicación global** bajo el modelo **cliente-servidor**, permitiendo que múltiples clientes se conecten a un mismo servidor y se comuniquen de forma simultánea sin depender de librerías externas.

El sistema incluye manejo de errores, conexión concurrente mediante hilos (`threading`) y lógica de **broadcast**, para que todos los usuarios reciban los mensajes en tiempo real.

---

### 🧩 Arquitectura del proyecto  
El proyecto se compone de dos scripts principales:

| Archivo | Rol | Descripción |
|----------|-----|-------------|
| `server.py` | Servidor | Acepta conexiones entrantes, administra los clientes y retransmite los mensajes (broadcast). |
| `client.py` | Cliente | Permite enviar y recibir mensajes simultáneamente desde la terminal. |

Modelo: **Cliente–Servidor**  
Protocolo: **TCP/IP (AF_INET + SOCK_STREAM)**  
Codificación: **UTF-8**

---

### ⚙️ Funcionamiento  

#### 🖥️ Servidor  
1. Crea un socket TCP (`socket.AF_INET`, `socket.SOCK_STREAM`).  
2. Se asocia a una IP (`localhost`) y un puerto (`8080`).  
3. Escucha conexiones entrantes y lanza un hilo por cliente.  
4. Reenvía cada mensaje recibido a todos los demás clientes (broadcast).  
5. Maneja desconexiones y errores (`ConnectionResetError`, `EOFError`, `KeyboardInterrupt`).

#### 💬 Cliente  
1. Se conecta al servidor mediante la IP y el puerto definidos.  
2. Solicita un nombre de usuario (username).  
3. Utiliza dos hilos: uno para enviar y otro para recibir mensajes.  
4. Los mensajes son codificados con UTF-8 antes de enviarse y decodificados al recibirse.  
5. Permite desconectarse escribiendo `salir`.

---

### 🧱 Características implementadas  
✅ Comunicación en tiempo real  
✅ Multiples clientes conectados simultáneamente  
✅ Threads para envío/recepción concurrente  
✅ Lógica de broadcast  
✅ Manejo de desconexiones y errores  
✅ Entrada/salida (stdin/stdout) desde consola  
✅ Uso de encoding UTF-8  
✅ Identificación de usuarios mediante username

---

### 🧠 Conceptos reforzados  
- Protocolos **TCP/IP**  
- Arquitectura **Cliente-Servidor**  
- Sockets en Python (`socket` module)  
- **Threading** y concurrencia  
- **Broadcast** y sincronización de mensajes  
- Flujo de datos en redes (entrada/salida estándar)  
- Manejo de errores y desconexiones seguras

---

### 🚀 Ejecución  

#### 1️⃣ Iniciar el servidor  
```bash
python server.py
```

#### 2️⃣ Iniciar los clientes (en diferentes terminales)
```bash
python client.py
```

#### 3️⃣ Enviar mensajes
Cada cliente puede escribir y enviar mensajes que serán recibidos por todos los demás.
Para salir:
```bash
salir
```

---

### 🧩 Tecnologías utilizadas
- Python 3.11

- Módulos estándar: socket, threading, sys

- Modelo: TCP (Orientado a conexión)

## 🇬🇧 English  
**The Huddle – Penguin Academy**

Author: Jimena Velázquez

### 📖 Description

This project implements a **real-time chat application** built from scratch using **TCP sockets** in Python.
The goal was to **rebuild global communication** through a **client-server** model, allowing multiple clients to connect and exchange messages concurrently without any external libraries.

The system includes error handling, multithreading (threading), and **broadcast** logic so that every client receives messages in real time.

---

### 🧩 Project Architecture

| File | Role | Description |
|----------|-----|-------------|
| `server.py` | Server | Accepts connections, manages clients, and broadcasts messages. |
| `client.py` | Client | Sends and receives messages simultaneously from the console. |

Model: **Client–Server**  
Protocol: **TCP/IP (AF_INET + SOCK_STREAM)**  
Encoding: **UTF-8**

---

### ⚙️ How it works  

#### 🖥️ Server 
1. Creates a TCP socket (`socket.AF_INET`, `socket.SOCK_STREAM`).  
2. Binds it to an IP (`localhost`) and port (`8080`).  
3. Listens for connections and spawns a thread per client.
4. Broadcasts received messages to all connected clients. 
5. Handles disconnections and exceptions (`ConnectionResetError`, `EOFError`, `KeyboardInterrupt`).

#### 💬 Client
1. Connects to the server using the specified IP and port.
2. Requests a username.
3. Uses two threads: one for sending and one for receiving messages
4. Messages are encoded and decoded using UTF-8. 
5. Typing `salir` disconnects the client.

---

### 🧱 Features
✅ Real-time communication  
✅ Multiple clients connected simultaneously  
✅ Multithreaded send/receive system  
✅ Broadcast message distribution  
✅ Error and disconnection handling  
✅ Command-line I/O (stdin/stdout)  
✅ UTF-8 encoding  
✅ Usernames for client identification

---

### 🧠 Key Concepts 
- **TCP/IP** protocols  
- **Client-Server** architecture. 
- Python (`socket` module)  
- **Multithreading** for concurrency  
- **Broadcast logic**
- **Standard I/O** for communication 
- **Error handling** and graceful shutdowns

---

### 🚀 How to Run 

#### 1️⃣ Start the server
```bash
python server.py
```

#### 2️⃣ Start the clients (in separate terminals)
```bash
python client.py
```

#### 3️⃣ Send messages

Every message from a client will be broadcasted to all others.
To disconnect:
```bash
salir
```

---

### 🧩 Technologies
- Python 3.11

- Standard libraries: **socket**, **threading**, **sys**

- Communication protocol: **TCP (connection-oriented)**
