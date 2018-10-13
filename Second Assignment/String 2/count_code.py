def count_code(str):
  i=0
  c=0
  for x in range(len(str)):
    x=str.find("co",i)
    if x!=-1:
      i=x+1
      if x+3<len(str)and str[x+3]=='e':
        c=c+1
  return c    
