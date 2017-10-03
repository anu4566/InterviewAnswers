import sys
import re
import os
import netaddr
import socket

ip_before_sorting = []
if sys.argv[1:]:
   print "File: %s" % (sys.argv[1])
   logfile = sys.argv[1]
else:
   logfile = raw_input("Please enter the file directories to parse, root/devops/ ")
for dirpath, dirnames, filenames in os.walk(logfile):
   for files in filenames:
      ips = []
      totalPath = dirpath+"/"+files
      #print (totalPath)
      file = open(totalPath, "r")
      for text in file.readlines():
         text = text.rstrip()
         count = 0
         regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
	 if regex is not None:
            for match in regex:
               if netaddr.valid_ipv4(match):
                  ips.append(match)
      
      seen = set()
      for ip in ips:
          key = tuple(ip.split(".")[:2])
          if key not in seen:
             ip_before_sorting.append(ip)
             seen.add(key)
      file.close()
finalIp = sorted(ip_before_sorting, key=lambda x:map(int, x.split('.')))
print (finalIp)
