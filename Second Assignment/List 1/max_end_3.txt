def max_end3(nums):
  if nums[0]>nums[-1]:
    return [nums[0] for x in range(len(nums))]
  else:
    return [nums[-1] for x in range(len(nums))]
      