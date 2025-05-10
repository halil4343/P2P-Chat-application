import socket
import json
import time
import os

PORT = 6000
peers = {}
PEER_TIMEOUT = 30  

def load_peers():
    try:
        with open('peers.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def save_peers():
    with open('peers.json', 'w') as f:
        json.dump(peers, f)

def listen_for_peers():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', PORT))

    print(f"🔍 Discovering peers on port {PORT}...")
    
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            ip = addr[0]
            
            try:
                msg = json.loads(data.decode())
                username = msg.get('username', 'unknown')
                
                # Update peer information
                if ip not in peers or peers[ip]['username'] != username:
                    print(f"✨ New peer found: {username} ({ip})")
                
                peers[ip] = {
                    'username': username,
                    'last_seen': time.time()
                }
                save_peers()
                
            except json.JSONDecodeError:
                continue
                
        except KeyboardInterrupt:
            print("Stopping discovery...")
            break
        except Exception as e:
            print(f"Discovery error: {e}")

if __name__ == "__main__":
    listen_for_peers()