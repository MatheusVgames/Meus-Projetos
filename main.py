meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "BUGOU": "Algo no pc travou",
            "MANO": "Você / ele, Tom informal entre pessoas do mesmo nivel"
            }
word = input("Digite uma palavra moderna que você não entende):").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
    # O que devemos fazer se a palavra for encontrada?
else:
    print("infelismente não temos o significado para esse meme")
    # O que devemos fazer se a palavra não for encontrada?
