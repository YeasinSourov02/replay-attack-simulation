import socket
import json

HOST = "127.0.0.1"
PORT = 5001

processed_ids = set()

def handle_message(data):
    message = json.loads(data)
    request_id = message.get("request_id")

    print("\n[SECURE SERVER] Received:", message)

    # Replay protection: reject a request ID that has already been used.
    if request_id in processed_ids:
        return {
            "status": "REJECTED",
            "message": "Replay detected: request has already been processed."
        }

    processed_ids.add(request_id)

    if message.get("action") == "TRANSFER":
        amount = message.get("amount")
        account = message.get("account")
        print(f"[SECURE SERVER] Processing transfer of {amount} BDT to {account}")
        return {
            "status": "SUCCESS",
            "message": f"Transfer of {amount} BDT to {account} processed."
        }

    return {"status": "ERROR", "message": "Unknown action"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"[SECURE SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"\n[SECURE SERVER] Connection from {addr}")
            data = conn.recv(4096).decode("utf-8")

            if not data:
                continue

            response = handle_message(data)
            conn.sendall(json.dumps(response).encode("utf-8"))
