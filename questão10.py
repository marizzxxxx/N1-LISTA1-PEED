#questão 9

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [float(num) for num in nums]

soma = sum(nums)
media = soma / len(nums)

print("A média é: ", media)