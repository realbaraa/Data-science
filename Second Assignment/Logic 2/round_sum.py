def round_sum(a, b, c):
  return round10_sum(a)+round10_sum(b)+round10_sum(c)
  
  



def round10_sum(n):
  if n%10 < 5:
    return 10*int(n/10)
  return 10* int((n+10)/10)
  
