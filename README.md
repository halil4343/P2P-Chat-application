# CMP2204 Term Project – P2P Chat Application

## Overview

This is a terminal-based peer-to-peer chat application developed for CMP2204: Introduction to Computer Networks. It follows the provided Functional Specification and implements the required four components:

- `announcer.py`: Broadcasts username over UDP every 8 seconds.
- `discovery.py`: Listens for peers on the network and maintains a list of known users.
- `initiator.py`: Allows the user to view online/away users, initiate chat (secure or unsecure), and view chat history.
- `responder.py`: Accepts incoming TCP chat messages and responds accordingly.

## Features

- UDP broadcast-based peer discovery.
- TCP-based peer-to-peer messaging.
- Optional secure chat using Diffie-Hellman key exchange.
- Message encryption and decryption (basic stub included).
- Chat logging with timestamps and direction (sent/received).

## How to Run

1. **Start the components in separate terminals** (or as background threads in the future):
   - `python announcer.py`
   - `python discovery.py`
   - `python responder.py`
   - `python initiator.py`

2. **Enter your username** when prompted by `announcer.py`.

3. **Use the menu in `initiator.py`** to view users, start a chat, or view chat history.

## Dependencies

- Python 3.6+
- No external libraries required (uses only standard Python modules)

## Files

- `announcer.py`: Sends presence messages to LAN.
- `discovery.py`: Listens and logs active peers.
- `responder.py`: Receives and handles chat messages.
- `initiator.py`: Provides menu interface for user actions.
- `chat_log.txt`: Shared log file.
- `peers.json`: Stores discovered peers.
- `README.md`: This documentation.
- `platform_notes.txt`: Platform info and team details.

## Known Limitations

- Message encryption is simulated with JSON wrapping; real encryption logic needs to be implemented.
- Diffie-Hellman key generation is basic and static.
- No GUI; all interaction is via the terminal.
- Error handling is minimal and may need improvements for production use.

