import socket
import threading

SERVER_IP = "192.168.1.53"
PORT = 5001

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print("\nClient disconnected.")
                break

            print(f"\nClient: {message}")
            print("Server: ", end="", flush=True)

        except:
            print("\nConnection closed.")
            break

# Create socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind
server_socket.bind((SERVER_IP, PORT))

# Listen
server_socket.listen(1)

print("Server started...")
print("Server IP: 192.168.1.53")
print("Port:", PORT)
print("Waiting for client...")

# Accept client
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)
print("You can now chat with the client.")
print("Type 'exit' to close.\n")


# Thread for receiving messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

receive_thread.daemon = True
receive_thread.start()

# Main thread sends messages
while True:
    message = input("Server: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break

client_socket.close()
server_socket.close()