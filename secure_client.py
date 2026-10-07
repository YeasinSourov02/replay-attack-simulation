import socket
import json

HOST = "127.0.0.1"
PORT = 5001

message = {
    "request_id": "REQ-1001",
    "action": "TRANSFER",
    "amount": 1000,
    "account": "STUDENT-001"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CLIENT] Sending request:")
    print(message)

    s.sendall(json.dumps(message).encode("utf-8"))

    response = s.recv(4096).decode("utf-8")
    print("[CLIENT] Server response:", response)
