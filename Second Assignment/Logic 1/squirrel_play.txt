def squirrel_play(temp, is_summer):
  r=range(60,91)
  r2=range(60,101)
  return (temp in r and not is_summer) or (is_summer and temp in r2)
