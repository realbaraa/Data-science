def cat_dog(str):
  i=0
  z=0
  c=0
  c2=0
  for x in range(len(str)):
    x=str.find("cat",i)
    y=str.find("dog",z)
    if x!=-1:
      i=x+2
      c=c+1
    if y!=-1:
      z=y+2
      c2=c2+1
  return c==c2