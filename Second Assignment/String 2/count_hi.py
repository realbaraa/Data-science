def count_hi(str):
  i=0
  c=0
  for x in range(len(str)):
    x=str.find("hi",i)
    if x!=-1:
      i=x+1
      c=c+1
  return c    
