def end_other(a, b):
  aa=a.lower()
  bb=b.lower()
  i=0
  for k in range(len(aa)):
    x=aa.find(bb,i)
    if x!=-1 :
      i=i+1
      if (x + len(bb)) == len(aa):
        return True
  i=0
  for k in range(len(bb)):
    x=bb.find(aa,i)
    if x!=-1:
      i=i+1
      if(x + len(aa)) == len(bb):
        return True
  return False
