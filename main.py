import threading
import discovery
import responder
import initiator
import time

def start_components():
    # Start discovery in background
    t1 = threading.Thread(target=discovery.listen_for_peers, daemon=True)
    t1.start()
    
    # Start responder in background
    t2 = threading.Thread(target=responder.start_server, daemon=True)
    t2.start()
    
    # Wait a moment for services to start
    time.sleep(1)
    
    # Start initiator in main thread (for user input)
    initiator.main_menu()

if __name__ == "__main__":
    print("🚀 Starting Simple P2P Chat...")
    start_components()