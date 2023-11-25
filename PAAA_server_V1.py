from ipaddress import *
import socket
import os
import random
import subprocess
import getpass
import ipaddress
from http import *
import socket
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

with open("psw.txt", "r") as tf:
    line1 = tf.read().split(",")

    
with open("usr.txt", "r") as tf:
    line2 = tf.read().split(",")


with open("ip.txt", "r") as tf:
    line3 = tf.read().split(",")
    
with open("email.txt", "r") as tf:
    line4 = tf.read().split(",")
    

    
#def pour regarder si l'email est bonne
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 

print("IIIIIIIIII             IIIIIIIIII                IIIIIIIIII                  IIIIIIIIII            ")
print("II       II           III      III              III      III                III      III                        ")
print("II       II          III        III            III        III              III        III                 ")
print("IIIIIIIIII          III          III          III          III            III          III                    ")
print("II                 IIIIIIIIIIIIIIIIII        IIIIIIIIIIIIIIIIII          IIIIIIIIIIIIIIIIII                                          ")
print("II                III              III      III              III        III              III                                 ")
print("II               III                III    III                III      III                III                                 ")


#Page de connexion

print("1 Connect")
print("2 Create an accunt")

#input pour le choix entre les deux
choice_accueil = input('')
if choice_accueil == '1':
    #Je demande username ou email et password
    email_connect = input("Email: ")
    password_connect = getpass.getpass("Password : ")
    
    #vérification du password de l'username et l'email
    if password_connect != line1 and  email_connect != line4:
        print("The password or the username are not good")
        print("You have stil 1 chance")
        email_connect = input("Email : ")
        password_connect = getpass.getpass("Password : ")
        if password_connect == line1 and email_connect == line4:
            result = subprocess.run(['python', '/Users/kids/Desktop/Garis/informatiuque/code/paaa v2/PAAA_home_V1.py'], capture_output=True, text=True)
            if result.returncode == 0:
                print("Le script a été exécuté avec succès.")
                print("Sortie standard :")
                print(result.stdout)
            else:
                print("Une erreur s'est produite lors de l'exécution du script.")
                print("Erreur standard :")
                print(result.stderr)
        

if choice_accueil == '2':
    username_nw_usr = input("Type your Username : ")
    with open('usr.txt', 'w') as fichier:
    # Demande à l'utilisateur ce qu'il veut écrire dans le fichier
        contenu = username_nw_usr
    
    # Écrit le contenu dans le fichier
        fichier.write(contenu)

    email_user = input("Type your Email address : ")
    check(email_user)
    with open('email.txt', 'w') as fichier:
    # Demande à l'utilisateur ce qu'il veut écrire dans le fichier
        contenu = email_user
    
    # Écrit le contenu dans le fichier
        fichier.write(contenu)
        
    psw_nw_usr = getpass.getpass("Type your password : ")
    with open('psw.txt', 'w') as fichier:
    # Demande à l'utilisateur ce qu'il veut écrire dans le fichier
        contenu = psw_nw_usr
    
    # Écrit le contenu dans le fichier
        fichier.write(contenu)



# Adresse IP et port d'écoute du serveur
HOST = '127.0.0.1'
PORT = 12345

# Création d'un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port
server_socket.bind((HOST, PORT))

# Attente de connexions entrantes
server_socket.listen()

print(f"Le serveur écoute sur {HOST}:{PORT}")

# Attente d'une connexion
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Envoi d'un message de confirmation au client
client_socket.sendall('Connexion réussie')
# Fermeture du socket serveur
server_socket.close()


