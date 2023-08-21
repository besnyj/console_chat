import socket
import threading
import functions
import utils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(utils.localhost)


nicknameInput = input("Choose a Nickname:\n")
client.send(functions.encrypt(nicknameInput).encode())


requests = threading.Thread(target=functions.requests, args=(client, nicknameInput))
responses = threading.Thread(target=functions.responses, args=(client, ))
requests.start()
responses.start()
