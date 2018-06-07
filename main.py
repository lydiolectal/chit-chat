import socket

HOST = ""
PORT = 12345

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        # listen for connections using TCP
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"I am connected to address: {addr}")
            while True:
                data = conn.recv(1024)
                if data:
                    data = data.decode("utf-8", "ignore")
                    print(f"Data received: {data}")
                    continue

def start_client():
    # TODO validate address
    host = input("Host IP address: ")
    port = int(input("Socket: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Say something: ")
            s.sendall(message.encode("utf-8"))

if __name__ == "__main__":
    while True:
        flag = input("c for client, s for server: ")
        if flag == "c" or flag == "s":
            break
    if flag == "c":
        start_client()
    else:
        start_server()
