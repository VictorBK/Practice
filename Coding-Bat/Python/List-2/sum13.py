def sum13(nums):
  total = 0
  n = 0
  while n < len(nums):
    if nums[n] == 13:
      n += 1
    else:
      total += nums[n]
    n += 1
  return total
