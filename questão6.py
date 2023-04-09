#questão 6

numeros = input("Digite a lista de números e separe por espaços: ")

numeros = numeros.split()

numeros = [int(numero) for numero in numeros]

soma = sum(numeros)

print("A soma dos números é:", soma)