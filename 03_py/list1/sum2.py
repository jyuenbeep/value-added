def sum2(nums):
  if len(nums)!=0:
    if len(nums)<2:
      return nums[0]
    else:
      return nums[0]+nums[1]
  return 0
