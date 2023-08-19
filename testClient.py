import socket
import threading
import utils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(utils.localhost)


nicknameInput = input("Choose a Nickname:\n")
client.send(nicknameInput.encode())


def responses():
    while True:
        response = client.recv(1024).decode()
        print(response)


def requests():

    while True:
        inputmessage = input()
        client.send(f'{nicknameInput}: {inputmessage}'.encode())


requests = threading.Thread(target=requests)
responses = threading.Thread(target=responses)
requests.start()
responses.start()
