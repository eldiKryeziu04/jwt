import socket
import jwt
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate RSA Keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("Server: Waiting for connections...")

    while True:
        client, addr = server.accept()
        data = client.recv(1024).decode().split()
        
        if not data: continue
        command = data[0]

        if command == "LOGIN":
            username, password = data[1], data[2]
            if username == "jane_doe" and password == "password123":
                # Create JWT
                token = jwt.encode({
                    "sub": username,
                    "iat": datetime.datetime.utcnow(),
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                }, private_key, algorithm="RS256")
                client.send(f"AUTH_SUCCESS {token}".encode())
            else:
                client.send(b"AUTH_FAIL")

        elif command == "GET_DATA":
            token = data[1]
            try:
                jwt.decode(token, public_key, algorithms=["RS256"])
                client.send(b"DATA { 'msg': 'Protected Python Data' }")
            except:
                client.send(b"ERROR 401 Unauthorized")
        client.close()

if __name__ == "__main__":
    start_server()