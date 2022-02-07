def leiaDinheiro(p):
    válido = False
    while not válido:
        entrada = str(input(p)).replace(',', '.').strip()
        if entrada .isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            válida = True
            return float(entrada)