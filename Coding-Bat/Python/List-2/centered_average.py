def centered_average(nums):
  nums.sort()
  set = nums[1:-1]
  return sum(set)//len(set)
