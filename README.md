# Basic Python Asyncio UDP Example

This is a **minimal Python project** demonstrating how to use **UDP with asyncio**.
It includes:

* A UDP **server** (listener) that prints received messages
* A UDP **client** (sender) that sends messages to the server
* Uses asyncio for asynchronous networking

Perfect for learning **UDP networking** and **asyncio basics**.

---

## Features

* Minimal and easy-to-read Python code
* Demonstrates `asyncio.DatagramProtocol`
* Infinite loops with `await asyncio.sleep()`
* Clean shutdown with task cancellation

---

## Files

* `udp_server.py` → The UDP server / listener
* `udp_client.py` → The UDP client / sender

---

## Requirements

* Python 3.7+
* asyncio (built-in with Python 3.7+)

---

## How to Run

### 1. Start the UDP Server

```bash
python udp_server.py
```

You should see:

```
Server listening on port 9999
```

### 2. Run the UDP Client

```bash
python udp_client.py
```

You should see on the server terminal:

```
Got message: Hello UDP! from ('127.0.0.1', 59316)
```

---

---
## Output:
### udp_server.py:
![alt text](image.png)

### udp_client.py:
![alt text](image-1.png)
---

## How it Works

* **Server**: listens on a port for incoming UDP packets and prints them
* **Client**: sends a message to the server using `transport.sendto()`
* **Transport**: handles sending the bytes
* **Protocol**: handles incoming data via `datagram_received`
* **Infinite loops**: `await asyncio.sleep()` keeps tasks alive without freezing the CPU

---

## Notes

* UDP is **connectionless**: packets may arrive out of order or be lost
* Source ports for the client may change each run (normal behavior)
* Ideal for learning **LAN broadcasts** and **lightweight messaging**

