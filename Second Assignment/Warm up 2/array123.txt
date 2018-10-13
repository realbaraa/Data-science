def array123(nums):
  str1 = ''.join(str(e) for e in nums)
  if str1.find("123")!=-1:
    return True
  return False  
    