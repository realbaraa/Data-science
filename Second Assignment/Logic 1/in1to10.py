def in1to10(n, outside_mode):
  r=range(1,11)
  if outside_mode :
    return n<=1 or n>=10
  return n in r
