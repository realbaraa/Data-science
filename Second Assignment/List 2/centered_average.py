def centered_average(nums):
  x=max(nums)
  y=min(nums)
  s=0
  c=0
  f=True
  f2=True
  for i in nums:
    if nums[c]==x and f:
      f=False
      c=c+1
      continue
    if nums[c]==y and f2:
      f2=False
      c=c+1
      continue
    s=s+i
    c=c+1
  return s/(c-2)
      
