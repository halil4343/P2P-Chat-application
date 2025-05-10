import socket
import threading
import json
import time
def get_username(ip):
    try:
        with open('peers.json', 'r') as f:
            peers = json.load(f)
            return peers.get(ip, {}).get('username', ip)
    except:
        return ip

def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        if data:
            message = data.decode()
            username = get_username(addr[0])
            print(f"\n📩 New message from {username}: {message}")
            
            # Simple logging
            with open('chat_log.txt', 'a') as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] FROM {username}: {message}\n")
                
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