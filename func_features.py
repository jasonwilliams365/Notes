nums = [1, 2, 3, 4, 5]

marliens = [x*x for x in nums]

eldians = list(filter(lambda x: x % 2 == 0, nums))    

print(marliens, eldians)