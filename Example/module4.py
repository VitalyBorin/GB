import re

s = input()

nums = re.findall(r'\d+', s)

nums = [int(i) for i in nums]

print(nums)