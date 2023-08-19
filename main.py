import socket
import threading
import utils

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(utils.localhost)
server.listen()

clientsList = []


class ClientAttr:
    def __init__(self, name):
        self.name = name


def broadcast(message):
    with open("log.txt", "a+") as f:
        f.write(f'{message.decode()}\n')
        f.close()
    for client in clientsList:
        client.send(message)


def communication(client, clientname):
    clientNick = clientname

    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clientsList.remove(client)
            broadcast(f'{clientNick} LEFT SESSION'.encode())
            utils.logger.info(f'{clientNick} DISCONNECTED')
            break


def handle():
    client, address = server.accept()
    clientsList.append(client)
    nickname = client.recv(1024).decode()
    clientobj = ClientAttr(nickname)
    broadcast(f'{clientobj.name} JOINED SESSION'.encode())
    utils.logger.info(f'{nickname} CONNECTED')
    clientname = clientobj.name

    t1 = threading.Thread(target=communication, args=(client, clientname,))
    t1.start()
    handle()


handle()
