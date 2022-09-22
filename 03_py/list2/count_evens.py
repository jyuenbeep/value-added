# https://codingbat.com/prob/p189616

"""
Return the number of even ints in the given array. Note: the % "mod" operator
computes the remainder, e.g. 5 % 2 is 1.
"""

def count_evens(nums):
  count = 0
  i = 0
  while i < len(nums):
    if nums[i] % 2 == 0:
      count += 1
    i += 1
  return count

  # test cases: do not edit
print(count_evens([2, 1, 2, 3, 4])) # 3
print(count_evens([2, 2, 0])) # 3
print(count_evens([1, 3, 5])) # 0
