def make_chocolate(small, big, goal):
  gm=goal%5
  if small>=gm:
    if big>=int(goal/5):
      return gm
    else :
      goal=goal-(big*5)
      if small>=goal:
        return goal
  return -1