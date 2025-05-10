import socket
import json
import time
import os

PORT = 6000
peers = {}

def listen_for_peers():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        try:
            msg = json.loads(data.decode())
            ip = addr[0]
            username = msg.get("username", "unknown")
            
            # Update or add peer
            if ip not in peers:
                print(f"📢 New user discovered: {username}")
            peers[ip] = {
                'username': username,
                'last_seen': time.time()
            }
            
            # Save to file (simple version)
            with open('peers.json', 'w') as f:
                json.dump(peers, f)
                
        except json.JSONDecodeError:
            continue

if __name__ == "__main__":
    listen_for_peers()