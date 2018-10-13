def last2(str):
  count=0
  comstr=str[len(str)-2:len(str)]

  for i in range(len(str)-2):
    com=str[i:i+2]
    if com==comstr:
      count=count+1
  return count


