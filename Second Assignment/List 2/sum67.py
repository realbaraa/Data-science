def sum67(nums):
  flag=True
  s=0
  for i in nums :
    if i==6:
      flag =False
    if i == 7 and not flag:
      flag=True
      continue
    if flag :
      s=s+i
  return s
