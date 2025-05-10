import threading
import time
import discovery
import responder
import initiator
import json
import os
import socket
def register_self(username):
    """Register our own username in peers.json"""
    peers = {}
    if os.path.exists('peers.json'):
        with open('peers.json', 'r') as f:
            peers = json.load(f)
    
    # Get local IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    
    peers[ip] = {
        'username': username,
        'last_seen': time.time()
    }
    
    with open('peers.json', 'w') as f:
        json.dump(peers, f)

def start_components(username):
    # Register ourselves first
    register_self(username)
    
    # Start services
    t1 = threading.Thread(target=discovery.listen_for_peers, daemon=True)
    t2 = threading.Thread(target=responder.start_server, daemon=True)
    
    t1.start()
    t2.start()
    
    # Wait a moment for services to start
    time.sleep(1)
    
    # Start initiator
    initiator.main_menu()

if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    print("🚀 Starting P2P Chat...")
    start_components(username)