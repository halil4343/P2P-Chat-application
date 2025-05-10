import json
import socket
import time

def load_peers():
    try:
        with open('peers.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def view_users():
    peers = load_peers()
    now = time.time()
    
    if not peers:
        print("No peers found yet")
        return
    
    print("\n=== Network Users ===")
    for ip, info in peers.items():
        username = info['username']
        last_seen = now - info['last_seen']
        
        if last_seen < 10:
            status = "🟢 Online"
        elif last_seen < 30:
            status = "🟡 Away"
        else:
            status = "⚪ Offline"
            
        print(f"- {username:20} {status} ({int(last_seen)}s ago)")

def chat_session(target, target_ip):
    print(f"\n🚀 Starting chat with {target} ({target_ip})")
    print("Type your messages (enter 'exit' to end)")
    
    while True:
        message = input("You: ")
        
        if message.lower() == 'exit':
            break
            
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target_ip, 6001))
                s.sendall(message.encode())
            
           
            with open('chat_log.txt', 'a') as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] TO {target}: {message}\n")
                
            print("Message sent!")
        except Exception as e:
            print(f"Failed to send: {e}")

def start_chat():
    peers = load_peers()
    
    if not peers:
        print("No peers available. Wait for discovery...")
        return
        
    view_users()
    target = input("\nEnter username to chat with: ").strip()
    
    # Find target
    target_ip = None
    for ip, info in peers.items():
        if info['username'].lower() == target.lower():
            target_ip = ip
            break
    
    if not target_ip:
        print(f"User '{target}' not found in network")
        return
    
    chat_session(target, target_ip)

def show_history():
    try:
        with open('chat_log.txt', 'r') as f:
            print("\n=== Chat History ===")
            print(f.read())
    except FileNotFoundError:
        print("No chat history yet")

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. View Network Peers")
        print("2. Start Chat")
        print("3. View Chat History")
        print("4. Exit")
        
        choice = input("Choose (1-4): ").strip()
        
        if choice == "1":
            view_users()
        elif choice == "2":
            start_chat()
        elif choice == "3":
            show_history()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    print("P2P Chat Application")
    main_menu()