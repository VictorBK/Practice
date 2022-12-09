def has22(nums):
  for n in range(len(nums)-1):
    if nums[n] == 2 and nums[n + 1] == 2:
      return True
  return False

