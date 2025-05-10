import socket
import threading
import time

def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        if data:
            message = data.decode()
            print(f"\n📩 New message: {message}")
            
            # Simple logging
            with open('chat_log.txt', 'a') as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] FROM {addr[0]}: {message}\n")
                
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 6001))
    server.listen()
    print("👂 Listening for messages on port 6001...")
    
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()