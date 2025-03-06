#!/usr/bin/python3
import socket
import sys

def httpget(DNS):
     
     host=DNS
     port=80
     request = "GET / HTTP/1.1\r\n" \
                "Host: " + host + "\r\n" \
                "Connection: close\r\n\r\n"
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try:
        s.connect((host, port))
     except Exception as e:
        print("Erreur dans la connexion des données")
        sys.exit(1)
     try:
        s.sendall(request.encode("utf-8"))
     except Exception as e:
        print("Erreur dans l'envoi des paquet")
        sys.exit(1)

     reponse =b""#Ici le b" indique qu'on va recevoir une réponse en bit
     while True :
        try:
            data= s.recv(4096)
        except Exception as e:
            print("Erreur dans le reception des données")
            sys.exit(1)
        if not data:
            print("La page est vide")
            break
        reponse+=data

     s.close()

     print(reponse.decode("utf-8"))

print(httpget(sys.argv[1]))
