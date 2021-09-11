frase = str(input("Digite uma frase: ")).lower().strip()
print("A letra A aparece {} vezes nessa frase".format(frase.count("a")))
print("A letra A aparece pela primeira vez na posição {}".format(frase.find("a")+1))
print("A letra A aparece pela última vez na posiçãõ {}".format(frase.rfind("a")+1))
