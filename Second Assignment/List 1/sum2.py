def sum2(nums):
  c=0
  c2=0
  for i in range(len(nums)):
    c=c+nums[i]
    c2=c2+1
    if c2==2:
      return c
  return c    
