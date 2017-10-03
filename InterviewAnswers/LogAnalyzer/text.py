import re

str = '1377123688|ERROR|handler.cpp|127|findHandlers|Division by zero'
occ = [m.start() for m in re.finditer('[^|]*',str)]
part1 = str[occ[4]:occ[5]]
print (part1)
