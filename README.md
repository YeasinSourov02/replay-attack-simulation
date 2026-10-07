# Replay Attack Simulation — Python Socket Programming

## Assignment
A controlled replay attack simulation using Python TCP sockets.

## Files
- `server.py` — vulnerable server
- `client.py` — legitimate client
- `attacker.py` — replays a previously captured valid request
- `secure_server.py` — server with simple replay protection
- `secure_client.py` — client containing a unique request ID

## Requirements
- Python 3
- No external packages

## Part 1: Normal communication
Terminal 1:
    python server.py

Terminal 2:
    python client.py

The server processes the legitimate transfer request.

## Part 2: Replay attack
Keep `server.py` running.

Terminal 3:
    python attacker.py

The attacker sends the same valid request again. Because the vulnerable server has no mechanism to determine whether the request was already processed, it processes the request a second time.

## Part 3: Prevention
Terminal 1:
    python secure_server.py

Terminal 2:
    python secure_client.py

Run the secure client once. It succeeds.

Then run:
    python secure_client.py

again with the same request ID. The secure server rejects the duplicate request as a replay.

## Security concept
A replay attack occurs when an attacker captures a valid communication and later retransmits it to cause the receiver to accept the old message again.

The vulnerable application lacks freshness/replay protection.

The demonstration uses a pre-recorded message rather than intercepting real traffic. Everything runs on localhost (127.0.0.1), satisfying the controlled-lab requirement.

## Important limitation
This is an educational simulation, not a real banking application. The transfer is only printed by the server; no real money or external system is involved.

## Possible stronger protections
Real systems can use nonces/challenge-response, timestamps with an acceptable time window, sequence numbers, unique transaction IDs, and authenticated integrity protection such as MACs/signatures. In practice, these mechanisms are usually combined with secure authenticated channels.
