#questão 11

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [int(num) for num in nums]

numpar = [ ]

for num in nums:
    if num % 2 == 0:
        numpar.append(num)
        
print("O número par da lista é:", numpar)