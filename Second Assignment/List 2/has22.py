def has22(nums):
  c=0
  for i in nums:
    if i == 2:
      c=c+1
    else : 
      c=0
    if c==2:
     return True
  return False
