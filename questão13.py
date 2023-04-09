#questão 13

palavras = input("Digite a lista de palavras e separe por espaços: ")

palavras = palavras.split()

palavraa = [ ]

for palavra in palavras:
    if palavra[0] == "a":
        palavraa.append(palavra)

print("Palavras que começam com a:", palavraa)