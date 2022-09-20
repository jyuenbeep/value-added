def array_front9(nums):
  aryLen = min(len(nums), 4)
  for i in range(aryLen):
    if nums[i]==9:
      return True
  return False
