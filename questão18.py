#questão 18

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

prod = 1

for num in nums:
    prod *= int(num)
 
print("O produto dos números, é:", prod)