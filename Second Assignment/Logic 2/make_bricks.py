def make_bricks(small, big, goal):
  gm=goal%5
  if small>=gm:
    if big>= int(goal/5):
      return True
    else :
      goal=goal-(big*5)
      if(small>=goal):
        return True
  if small>=goal:
    return True
  return False
    
    

