#!/usr/bin/python3
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("37.59.174.225",21))

print ("Conectando ao Servidor...")
banner = tcp.recv(1024)
print (banner)

print ("Enviando Usuario...")
tcp.send ("USER ftp\r\n")
user = tcp.recv(1024)
print (user)

print ("Enviando a Senha...")
tcp.send ("PASS ftp\r\n")
pw = tcp.recv(1024)
print (pw)

print ("Enviando comando HELP ...")
tcp.send ("HELP\r\n")
cmd = tcp.recv(2048)
print (cmd)
