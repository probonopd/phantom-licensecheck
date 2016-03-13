#!/usr/bin/python
# Split DJI firmware package file into different modules
# dji_split.py <name.bin>

from struct import *
import hashlib
import sys

def copypart(src,dest,start,length,bufsize=1024*1024):
    with open(src,'rb') as f1:
        f1.seek(start)
        with open(dest,'wb') as f2:
            while length:
                chunk = min(bufsize,length)
                data = f1.read(chunk)
                f2.write(data)
                length -= chunk

djifile=sys.argv[1]

f=open(djifile,'rb')
if 1==1:  # todo only use valid dji firmware package files
	f.seek(44)									# number of rows
	num=unpack('<H',f.read(2))[0]
	i=0
	while i<num:
		base=64+i*52
		f.seek(base)
		namepart=f.read(2).encode("hex")		# module typ
		f.seek(base+8)
		star=unpack('<I',f.read(4))[0]				# start of firmware module
		leng=unpack('<I',f.read(4))[0]				# length of firmware module
		copypart(djifile,namepart+"_"+os.path.basename(djifile),star,leng)
		i=i+1
else: 
	print "ERROR, invalid file"

f.close()