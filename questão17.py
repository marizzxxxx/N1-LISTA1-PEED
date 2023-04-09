#questão 17

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

numimpars = 0

for num in nums:
    if int(num) % 2 == 1:
        numimpars += int(num)
 
print("A soma dos números impares da lista são:", numimpars)