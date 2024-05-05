# client.py

import socket
import json
import pprint

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.client_socket.connect((host, port))

    def request(self, request_objs):
        request_data = json.dumps(request_objs).encode()
        self.client_socket.sendall(request_data)
        response_data = self.client_socket.recv(4096)
        responses = json.loads(response_data.decode())
        return responses

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = Client()
    client.connect("localhost", 9999)

    num_requests = int(input("Enter the number of requests: "))
    requests = []
    for i in range(num_requests):
        command = input(f"Enter command {i+1}: ")
        request_obj = {
            "method": command,
            "id": f"{i+1}",
        }
        requests.append(request_obj)

    response = client.request(requests)
    for res in response:
        print(f'id: {res.get("id")} response:{res.get("stdout",None)}')

    client.close()
