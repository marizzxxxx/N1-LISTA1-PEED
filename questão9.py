#questão 9

nums = input("Digite a lista de números e separe por espaços: ")

nums = nums.split()

nums = [int(num) for num in nums]

mnum = nums[0]

for num in nums:
    if num < mnum:
        mnum = num
        
print("O menor número da lista é:", mnum)