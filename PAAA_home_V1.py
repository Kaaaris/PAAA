import os
import subprocess
import random

print("IIIIIIIIII             IIIIIIIIII                IIIIIIIIII                  IIIIIIIIII            ")
print("II       II           III      III              III      III                III      III                        ")
print("II       II          III        III            III        III              III        III                 ")
print("IIIIIIIIII          III          III          III          III            III          III                    ")
print("II                 IIIIIIIIIIIIIIIIII        IIIIIIIIIIIIIIIIII          IIIIIIIIIIIIIIIIII                                          ")
print("II                III              III      III              III        III              III                                 ")
print("II               III                III    III                III      III                III                                 ")


choice_home = input("1 app  2 document  3 app server  4 Settings")
if choice_home == '1':
        choice_home_app = input("1 Note")
        if choice_home_app == '1':
            result = subprocess.run(['python', '/Users/kids/Desktop/Garis/informatiuque/code/python/todo.py'], capture_output=True, text=True)
            if result.returncode == 0:
                print("Sortie standard :")
                print(result.stdout)
                
            else:
                
                print("Erreur standard :")
                print(result.stderr)
        