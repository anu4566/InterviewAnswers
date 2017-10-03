import sys
import re
import os
import operator

if sys.argv[1:]:
   print "File: %s" % (sys.argv[1])
   logfile = sys.argv[1]
else:
   logfile = raw_input("Please enter a log files directory to parse, e.g /root/devops/ ")
mapVal = {}
for dirpath, dirnames, filenames in os.walk(logfile):
   for files in filenames:
      if files.endswith(".log"):
         totalPath = dirpath+"/"+files
         file = open(totalPath, "r")
         for text in file.readlines():
            text = text.strip()
            if 'ERROR' in text:
               occ = [m.start() for m in re.finditer('[^|]*',text)]
	       part1 = text[occ[4]:occ[5]]
	       key = part1.strip()
	       if key in mapVal:
	          mapVal[key] += 1
		  updateVal = {key: mapVal[key]}
                  mapVal.update(updateVal)
               else:
		  count = 1
		  newVal = {key: count}
                  mapVal.update(newVal)

sortedMap = sorted(sorted(mapVal.iteritems()), key=operator.itemgetter(1), reverse=True)
print (sortedMap)
