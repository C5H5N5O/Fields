from contextlib import redirect_stderr
import socket
import threading


IP = socket.gethostbyname(socket.gethostname())
PORT = 8000

class Server():

    sock = socket.socket()
    devices = {}
    devision_simbhol = "[!]"

    def __init__(self, host, port):
        self.host = host
        self.port = port


    def start_server(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen()


    def listen_connections(self):
        while True:
            host, addr = self.sock.accept()
            name = host.recv(2048).decode("utf-8")

            self.devices[name] = host
            print(f"device {name} has connected. ip: {addr}")

            threading.Thread(target=self.listen, args=(name,))


    def listen(self, name):
        while True:
            request = self.devices[name].recv(2048).decode("utf-8")
            print(f"{name}: '{request}'")

            self.serve_request(request)


    def send(self, name, request):
        self.devices[name].send(request.encode("utf-8"))
            
    
    def serve_request(self, request):
        name, command = request.split(self.devision_simbhol)

        if name == "SERVER":
            pass

        self.send(self.devices[name], command)
    
    
    

if __name__ == "__main__":
    server = Server(IP, PORT)
    server.start_server()
    print(f"Server started on {server.host}:{server.port}")

    threading.Thread(target=server.listen_connections,).start()
    
    