def xyz_there(str):
  i=0
  for l in range(len(str)):
    x=str.find("xyz",i)
    if x!=-1:
      i=i+1
      if str[x-1]!='.' and x!=0:
        return True
      elif x==0:
        return True
  return False
