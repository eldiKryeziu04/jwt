import socket

def run_client():
    token = None
    user = input("Enter username: ")
    pw = input("Enter password: ")

    # Authentication Step
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 5000))
    s.send(f"LOGIN {user} {pw}".encode())
    resp = s.recv(4096).decode()
    
    if resp.startswith("AUTH_SUCCESS"):
        token = resp.split()[1]
        print(f"Logged in. Token: {token}")
        
        while True:
            cmd = input("\nCommands: 'request_data', 'logout': ")
            if cmd == "request_data":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('localhost', 5000))
                s.send(f"GET_DATA {token}".encode())
                print(f"Server: {s.recv(1024).decode()}")
            elif cmd == "logout":
                print("Session cleared.")
                break
    else:
        print("Login failed.")

if __name__ == "__main__":
    run_client()