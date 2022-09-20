def centered_average(nums):
  nums.sort()
  i = 0
  total = 0
  while i < len(nums):
    if i != 0 and i != len(nums) - 1:
      total += nums[i]
    i += 1
  return total / (len(nums)-2)
