import threading
import utils
import random


clientsList = []


class ClientAttr:
    def __init__(self, name):
        self.name = name


def encrypt(message):

    alphabetCharacters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ':']
    alphabetCharactersShuffled = alphabetCharacters.copy()

    shuffleNumber = random.randint(1000, 9999)
    random.Random(shuffleNumber).shuffle(alphabetCharactersShuffled)

    encryptedOutcome = ""

    for character in message:
        encryptedCharacter = alphabetCharactersShuffled[alphabetCharacters.index(character)]
        encryptedOutcome = f'{encryptedOutcome}{encryptedCharacter}'

    encryptedOutcome = f'{shuffleNumber} {encryptedOutcome}'

    return encryptedOutcome


def decrypt(message):

    alphabetCharacters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ':']
    alphabetCharactersShuffled = alphabetCharacters.copy()

    shuffleNumber = int(str(message.split()[0]))
    random.Random(shuffleNumber).shuffle(alphabetCharactersShuffled)

    decryptedOutcome = ""

    testText = message

    for character in testText[5:]:
        decryptedCharacter = alphabetCharacters[alphabetCharactersShuffled.index(character)]
        decryptedOutcome = f'{decryptedOutcome}{decryptedCharacter}'

    return decryptedOutcome


def responses(client):
    while True:
        response = decrypt(client.recv(1024).decode())
        print(response)


def requests(client, nicknameInput):
    while True:
        inputmessage = input()
        client.send(encrypt(f'{nicknameInput}: {inputmessage}').encode())


def broadcast(message):
    message = encrypt(message)
    for client in clientsList:
        client.send(message.encode())


def communication(client, clientname):
    clientNick = clientname
    while True:
        try:
            message = decrypt(client.recv(1024).decode())
            broadcast(message)
        except:
            clientsList.remove(client)
            broadcast(f'{clientNick} LEFT SESSION')
            utils.logger.info(f'{clientNick} DISCONNECTED')
            break


def handle(server):
    client, address = server.accept()
    clientsList.append(client)
    nickname = decrypt(client.recv(1024).decode())
    clientobj = ClientAttr(nickname)
    utils.logger.info(f'{nickname} CONNECTED')
    broadcast(f'{clientobj.name} JOINED SESSION')
    clientname = clientobj.name

    t1 = threading.Thread(target=communication, args=(client, clientname,))
    t1.start()
    handle(server)
