#questão 7

palavras = input("Digite a lista de palavras e separe por espaços: ")

palavras = palavras.split()

pg = ""

for palavra in palavras:
    
    if len(palavra) > len(pg):
        
        pg = palavra
        
print("A palavra mais longa é:", pg)
