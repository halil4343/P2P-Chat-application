import socket
import time
import json

def start_announcer(username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    print(f"📢 Announcing as '{username}' every 8 seconds...")
    
    while True:
        message = json.dumps({"username": username})
        sock.sendto(message.encode(), ('255.255.255.255', 6000))
        time.sleep(8)

if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    start_announcer(username)