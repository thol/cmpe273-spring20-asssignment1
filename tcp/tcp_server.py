import socketserver

class ClientProcessor(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(bytes('pong',"utf-8"))


if __name__ == "__main__":
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5000
    BUFFER_SIZE = 1024
    
    with socketserver.TCPServer((TCP_IP,TCP_PORT), ClientProcessor) as server:
        server.serve_forever()