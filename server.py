import socket
import json

HOST = "127.0.0.1"
PORT = 5000

def handle_message(data):
    message = json.loads(data)

    print("\n[SERVER] Received:", message)

    # Vulnerability: the server does NOT check whether this
    # request has already been processed.
    if message.get("action") == "TRANSFER":
        amount = message.get("amount")
        account = message.get("account")
        print(f"[SERVER] Processing transfer of {amount} BDT to {account}")
        return {
            "status": "SUCCESS",
            "message": f"Transfer of {amount} BDT to {account} processed."
        }

    return {"status": "ERROR", "message": "Unknown action"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"\n[SERVER] Connection from {addr}")
            data = conn.recv(4096).decode("utf-8")

            if not data:
                continue

            response = handle_message(data)
            conn.sendall(json.dumps(response).encode("utf-8"))
