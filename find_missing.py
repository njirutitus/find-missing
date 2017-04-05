def find_missing(a,b):
  if len(a) != len(b) :
    c = set(a)^set(b)
    for d in c:
  	  return d
  else:
  	return 0
   
