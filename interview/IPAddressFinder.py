import sys
import re

try:
    if sys.argv[1:]:
        print "File: %s" % (sys.argv[1])
        logfile = sys.argv[1]
    else:
        logfile = raw_input("Please enter a log file to parse, e.g /var/log/secure: ")
    try:
	print (logfile)
        for dirpath, dirnames, filenames in os.walk(logfile):
           print (filenames)
	   ips = []
	   for files in filenames:
	      print (files)
              for text in files.readlines():
                 text = text.rstrip()
                 regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$',text)
                 if regex is not None and regex not in ips:
                    ips.append(regex)

           for ip in ips:
               outfile = open("/tmp/list.txt", "a")
               addy = "".join(ip)
               if addy is not '':
                  print "IP: %s" % (addy)
                  outfile.write(addy)
                  outfile.write("\n")
    finally:
	files.close()
        outfile.close()
except IOError, (errno, strerror):
        print "I/O Error(%s) : %s" % (errno, strerror)
