def no_teen_sum(a, b, c):
  r=range(13,20)
  if a in r :
    a=fix_teen(a)
  if b in r :
    b=fix_teen(b)
  if c in r:
    c=fix_teen(c)
  return a+b+c


def fix_teen(n):
  if n==16 or n==15:
    return n
  return 0