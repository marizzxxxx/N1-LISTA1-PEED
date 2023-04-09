#questão 8

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

numg = ""

for num in nums:
    
    if len(num) > len(numg):
        
        numg = num
        
print("O maior número é:", numg)
