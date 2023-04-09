#questão 16

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

numpars = 0

for num in nums:
    if int(num) % 2 == 0:
        numpars += int(num)
 
print("A soma dos números pares da lista são:", numpars)