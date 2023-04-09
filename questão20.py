#questão 20

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [int(num) for num in nums]

nums.sort(reverse=True)
 
print("A lista em ordem decrescente é:", nums)