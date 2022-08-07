def count_0s(list):
  midpoint = len(list)//2
  zeros = 0
  if len(list) == 1:
    if list[0] == 0:
      zeros += 1
  elif list[midpoint] == 0:
    zeros += len(list[:midpoint+1])
    zeros += count_0s(list[midpoint+1:])
  elif list[midpoint] == 1:
    zeros += count_0s(list[:midpoint])
  return zeros

binary = [0,0,0,0,1,1,1]
print(binary.index(1))
print(count_0s(binary))