def xo(s):
  #same = None
  smalls = s.lower()
  smalls_x = [i for i in range(0, len(smalls)) if i == 'x']
  smalls_o = [j for j in range(0, len(smalls)) if j == 'o']
  if len(smalls_x) == len(smalls_o):
    print(True)
  else:
    print(False)