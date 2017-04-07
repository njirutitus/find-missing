def find_missing(a,b):
  """find items which are in one list but not in the other """
  if len(a) != len(b) :
    c = set(a)^set(b)
    for d in c:
  	  return d
  else:
  	return 0
   
