#questão 19

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [int(num) for num in nums]

nums.sort()
 
print("A lista em ordem crescente é:", nums)