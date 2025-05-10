import socket
import time
import json

def start_announcer(username):
    BROADCAST_IP = '192.168.1.255'  # Mandatory broadcast address
    PORT = 6000
    INTERVAL = 8  # Every 8 seconds as required
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    print(f"📢 Announcing as '{username}' to {BROADCAST_IP} every {INTERVAL}s")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            message = json.dumps({
                "username": username,
                "timestamp": time.time()
            })
            sock.sendto(message.encode(), (BROADCAST_IP, PORT))
            print(f"[{time.strftime('%H:%M:%S')}] {username} announced to {BROADCAST_IP}")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nAnnouncer stopped")
    finally:
        sock.close()

if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    start_announcer(username)