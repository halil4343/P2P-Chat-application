import socket
import time
import json

def get_broadcast_address():
    """Get the appropriate broadcast address for the network"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Connect to Google DNS
        ip = s.getsockname()[0]
        s.close()
        # Create broadcast address from IP (works for most home networks)
        return '.'.join(ip.split('.')[:-1] + ['255'])
    except:
        return '255.255.255.255'  # Fallback to universal broadcast

def start_announcer(username):
    PORT = 6000
    INTERVAL = 8
    
    # Get the right broadcast address for this network
    broadcast_ip = get_broadcast_address()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('0.0.0.0', 0))  # Bind to all interfaces
    
    print(f"🔊 Announcing as '{username}' to {broadcast_ip} every {INTERVAL}s")
    
    try:
        while True:
            message = json.dumps({"username": username})
            sock.sendto(message.encode(), (broadcast_ip, PORT))
            print(f"{username} is online at {broadcast_ip}")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nStopping announcer")
    finally:
        sock.close()

if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    start_announcer(username)