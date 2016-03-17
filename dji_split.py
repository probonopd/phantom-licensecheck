#!/usr/bin/python
# Split DJI firmware package file into different modules
# dji_split.py <name.bin>

from struct import *
import glob
import hashlib
import sys
import os

# copy specific part of a file

def copypart(src,dest,start,length,bufsize=1024*1024):
    with open(src,'rb') as f1:
        f1.seek(start)
        with open(dest,'wb') as f2:
            while length:
                chunk = min(bufsize,length)
                data = f1.read(chunk)
                f2.write(data)
                length -= chunk
    f1.close()
    f2.close()

# start main execution

for djifile in sys.argv:
	f=open(djifile,'rb')
	if unpack('I', f.read(4))[0]==0x12345678:  # todo only use valid dji firmware package files
		f.seek(44)									# number of rows
		num=unpack('<H',f.read(2))[0]
		i=0
		while i<num:
			base=64+i*52
			f.seek(base)
			namepart=f.read(2).encode("hex")		# module typ
			f.seek(base+4)
			vers="."+str(ord(f.read(1)))					# version
			vers="."+str(ord(f.read(1)))+vers
			vers="."+str(ord(f.read(1)))+vers
			vers="V"+str(ord(f.read(1)))+vers
			print vers
			f.seek(base+8)
			star=unpack('<I',f.read(4))[0]				# start of firmware module
			leng=unpack('<I',f.read(4))[0]				# length of firmware module
			copypart(djifile,namepart+"_"+vers+"_"+os.path.basename(djifile),star,leng)
			i=i+1
	f.close()