def array_front9(nums):
  lenn=4
  if len(nums)<4:
    lenn=len(nums)
  for i in range(lenn):
    if nums[i]==9:
      return True
  return False
