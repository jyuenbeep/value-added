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
