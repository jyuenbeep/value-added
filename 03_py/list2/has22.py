def has22(nums):
  i = 0
  mode = 0
  while i < len(nums):
    if i != len(nums) - 1:
      if nums[i] == 2:
        if nums[i+1] == 2:
          return True
          mode = 1
    i += 1
  if mode == 0:
    return False
