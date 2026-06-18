import random

caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Numero_de_caracteres = input("digite o numero de caracteres:")
if Numero_de_caracteres.isdigit():
    Numero_de_caracteres = int(Numero_de_caracteres)
    senha = ""
    for i in range(Numero_de_caracteres):
        senha += random.choice(caracteres)
    print("sua senha é:", senha)