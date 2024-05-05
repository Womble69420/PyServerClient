# server.py

import socket
import json
import subprocess
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(4096)
        if request_data:
            try:
                requests = json.loads(request_data.decode())
                responses = []
                for request in requests:
                    method = request.get("method")
                    command_id = request.get("id")
                    if method:
                        result, stdout, stderr = self.execute_command(method)
                        response = {
                            "result": result,
                            "stdout": stdout,
                            "stderr": stderr,
                            "id": command_id,
                            "error_code": 0  # No error
                        }
                    else:
                        response = {
                            "error_code": 2,  # Invalid request
                            "id": command_id
                        }
                    responses.append(response)

            except json.JSONDecodeError:
                responses = [{
                    "error_code": 1,  # JSON parse error
                    "id": None
                }]

            response_data = json.dumps(responses).encode()
            client_socket.sendall(response_data)
        client_socket.close()

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)

if __name__ == "__main__":
    server = Server("localhost", 9999)
    server.start()
