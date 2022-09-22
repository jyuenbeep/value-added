# https://codingbat.com/prob/p166170

"""
Given an array of ints, return the number of 9's in the array.
"""

def array_count9(nums):
  countNine=0;
  for i in nums:
    if i==9:
      countNine+=1
  return countNine

  # test cases: do not edit
print(array_count9([1, 2, 9])) # 1
print(array_count9([1, 9, 9])) # 2
print(array_count9([1, 9, 9, 3, 9])) # 3
