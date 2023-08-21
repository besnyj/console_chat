import socket
import utils
import functions

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(utils.localhost)
server.listen()


functions.handle(server)
