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
            print(f"\n💬 Message from {username}: {message}")
            
            # Log the message
            with open('chat_log.txt', 'a') as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] FROM {username}: {message}\n")
                
    except Exception as e:
        print(f"Error handling message: {e}")
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 6001))
    server.listen()
    
    print(f"🛟 Chat responder running on port 6001")
    print("Waiting for incoming messages...")
    
    while True:
        try:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
        except KeyboardInterrupt:
            print("Shutting down responder...")
            break
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()