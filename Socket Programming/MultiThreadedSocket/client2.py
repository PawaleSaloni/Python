import socket
import threading

# Create client socket
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  #IPv4. #TCP

print("Waiting to Connected to server!")

# Connect to Windows server
client.connect(("192.168.1.53", 5000))

print("Connected to server!")

# Receive messages from server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                print("\nServer disconnected.")
                break
            print("\nServer:", message)
        except:
            break

# Start receiving in background
thread = threading.Thread(target=receive_messages)
# Thread is stopped when program exits
thread.daemon = True
thread.start()

# Main Thread
# Send messages to server
while True:
    message = input("You: ")
    if message.lower() == "exit":
        break
    client.send(message.encode())
client.close()