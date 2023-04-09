#questão 14

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

num10 = [ ]

for num in nums:
    if float(num) > 10:
        num10.append(num)
       
print("Os números maiores que 10 da lista são:", num10)