def count_evens(nums):
  sum = 0
  for num in nums:
    if num % 2 == 0:
      sum += 1
  return sum
