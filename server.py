import socket

# Server IP and port
SERVER_IP = "192.168.1.53"
PORT = 5001

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to IP and port
server_socket.bind((SERVER_IP, PORT))

# Start listening
server_socket.listen(1)

print("Server started...")
print("Server IP:", SERVER_IP)
print("Port:", PORT)
print("Waiting for client connection...")

# Accept client
client_socket, client_address = server_socket.accept()

print("Client connected!")
print("Client IP and Port:", client_address)

# Receive message from client
message = client_socket.recv(1024).decode()

print("Message from client:", message)

# Send response to client
response = "Hello Client! Message received by Server."

client_socket.send(response.encode())

# Close connection
client_socket.close()
server_socket.close()

print("Connection closed.")