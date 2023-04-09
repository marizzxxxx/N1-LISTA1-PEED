#questão 12

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [int(num) for num in nums]

numimpar = [ ]

for num in nums:
    if num % 2 == 1:
        numimpar.append(num)
        
print("O número impar da lista é:", numimpar)