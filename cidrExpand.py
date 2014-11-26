#!/usr/bin/env python
#Jeremy Galloway // root at cypherg dot com

from netaddr import IPNetwork
import sys

if len(sys.argv) < 2:
	print 'example usage: python cidrExpand.py cidrRanges.txt >> output.txt'
	
with open(sys.argv[1], 'r') as cidrRanges:
	for line in cidrRanges:
		ip = IPNetwork(line)
		for ip in ip:
			print ip

cidrRanges.close()
exit()