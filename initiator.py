import json
import time
import socket

def load_peers():
    try:
        with open('peers.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def view_users():
    peers = load_peers()
    now = time.time()
    print("\n=== Online Users ===")
    for ip, info in peers.items():
        username = info['username']
        last_seen = info['last_seen']
        status = "Online" if (now - last_seen) < 10 else "Away"
        print(f"- {username} ({status})")

def save_message(username, message, direction):
    with open('chat_log.txt', 'a') as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {direction} {username}: {message}\n")

def start_chat():
    peers = load_peers()
    target = input("\nEnter username to chat with: ")
    
    # Find target IP
    target_ip = None
    for ip, info in peers.items():
        if info['username'].lower() == target.lower():
            target_ip = ip
            break
    
    if not target_ip:
        print("❌ User not found!")
        return
    
    message = input("Type your message: ")
    
    try:
        # Simple TCP connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((target_ip, 6001))
            s.sendall(message.encode())
        print("✅ Message sent!")
        save_message(target, message, "TO")
    except Exception as e:
        print(f"❌ Failed to send: {e}")

def show_history():
    try:
        with open('chat_log.txt', 'r') as f:
            print("\n=== Chat History ===")
            print(f.read())
    except:
        print("No history yet")

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. View Online Users")
        print("2. Start Chat")
        print("3. View History")
        print("4. Exit")
        
        choice = input("Choose (1-4): ")
        
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
    main_menu()