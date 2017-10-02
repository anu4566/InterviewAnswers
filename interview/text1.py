import sys
import re
import os
import netaddr
import socket

if sys.argv[1:]:
   print "File: %s" % (sys.argv[1])
   logfile = sys.argv[1]
else:
   logfile = raw_input("Please enter a log file to parse, e.g /var/log/secure: ")
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

      finalIp = sorted(ips, key=lambda x:map(int, x.split('.')))
      for ip in finalIp:
         print(ip)
      file.close()
