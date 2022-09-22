# https://codingbat.com/prob/p108886

"""
Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed by at
least one 7). Return 0 for no numbers.
"""

def sum67(nums):
  i = 0
  count = 0
  mode = 0
  while i < len(nums):
    if mode == 0:
      if nums[i] == 6:
        mode = 1
      else:
        count += nums[i]
    else:
      if nums[i] != 7:
        count += 0
      else:
        mode = 0
    i += 1
  return count

  # test cases: do not edit
print(sum67([1, 2, 2])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7, 2])) # 4
