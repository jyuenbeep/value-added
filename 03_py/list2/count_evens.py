def count_evens(nums):
  count = 0
  i = 0
  while i < len(nums):
    if nums[i] % 2 == 0:
      count += 1
    i += 1
  return count
