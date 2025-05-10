import socket
import time
import json

BROADCAST_IP = '192.168.1.255'  # Removed leading space
PORT = 6000
INTERVAL = 8  

def start_announcer(username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Set timeout to prevent indefinite blocking
    sock.settimeout(0.2)
    
    print(f"📢 Starting announcer as '{username}' ({BROADCAST_IP})")
    print(f"Broadcasting every {INTERVAL} seconds...")
    print("Press Ctrl+C to stop\n")

    try:
        while True:
            message = json.dumps({
                "username": username,
                "ip": BROADCAST_IP,
                "timestamp": time.time()
            })
            
            try:
                sock.sendto(message.encode(), (BROADCAST_IP, PORT))
                print(f"[{time.strftime('%H:%M:%S')}]  '{username}' ({BROADCAST_IP}) announced")
            except socket.error as e:
                print(f"Broadcast error: {e}")
            
            time.sleep(INTERVAL)
            
    except KeyboardInterrupt:
        print("\nStopping announcer...")
    finally:
        sock.close()

if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    start_announcer(username)