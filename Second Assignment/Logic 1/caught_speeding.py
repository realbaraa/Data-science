def caught_speeding(speed, is_birthday):
  s=range(0,61)
  s2=range(61,81)
  if is_birthday:
    speed=speed-5
  if speed in s:
    return 0
  elif speed in s2:
    return 1
  return 2
