#questão 15

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

num5 = [ ]

for num in nums:
    if float(num) < 5:
        num5.append(num)
 
print("Os números menores que 5 da lista são:", num5)