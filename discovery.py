import socket
import json
import time
import os

PORT = 6000
peers = {}

def listen_for_peers():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', PORT))  # Listen on all interfaces
    
    print(f"👂 Listening for peers on port {PORT}...")
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            ip = addr[0]
            
            try:
                msg = json.loads(data.decode())
                username = msg.get("username", "unknown")
                
                if ip not in peers:
                    print(f"✨ Discovered: {username} ({ip})")
                
                peers[ip] = {
                    'username': username,
                    'last_seen': time.time()
                }
                
                # Save peers to file
                with open('peers.json', 'w') as f:
                    json.dump(peers, f)
                    
            except json.JSONDecodeError:
                print("Received invalid message")
                
    except KeyboardInterrupt:
        print("\nStopping discovery")
    finally:
        sock.close()

if __name__ == "__main__":
    listen_for_peers()