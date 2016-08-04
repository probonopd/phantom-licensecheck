import os
import sys
import argparse
import binascii

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()

f = open(args.echo, 'rb')

ft = f.read()
ft_head = ft[:64]
str_num = ord(ft_head[44])
#ft_body = ft[64 + 52 * str_num:]
print "FILE LEN = ", len(ft)

for i in range(str_num):
    ft_info = ft[64 + 52 * i: 64 + 52 * ( i + 1 )]
    ft_info_type = ft[64 + 52 * i: 65 + 52 *  i ].encode('hex')
    ft_info_type_ver_1 = int(binascii.b2a_hex(ft[71 + 52 * i: 72 + 52 *  i ]),16)
    ft_info_type_ver_2 = int(binascii.b2a_hex(ft[70 + 52 * i: 71 + 52 *  i ]),16)
    ft_info_type_ver_3 = int(binascii.b2a_hex(ft[69 + 52 * i: 70 + 52 *  i ]),16)
    ft_info_type_ver_4 = int(binascii.b2a_hex(ft[68 + 52 * i: 69 + 52 *  i ]),16)
    
    start_addr = 0
    for j in range(8,12):
        start_addr += ord(ft_info[j]) * ( 256 ** ( j - 8 ) )
    ft_ilen = 0
    for j in range(12,16):
        ft_ilen += ord(ft_info[j]) * ( 256 ** ( j - 12 ) )
    ft_ibody = ft[start_addr:start_addr + ft_ilen]
    print "---", i, " ---"
    print "WRITE TO ", ft_info_type + '.hex'
    print "START:   ", start_addr
    print "FINISH:  ", start_addr + ft_ilen - 1
    print "LEN:     ", ft_ilen
    print "TYPE:    ", ft_info_type
    print "VERSION: ", ft_info_type_ver_1,".",ft_info_type_ver_2,".",ft_info_type_ver_3,".",ft_info_type_ver_4 

    fi = open( ft_info_type + '_(' + str(ft_info_type_ver_1) + '.' + str(ft_info_type_ver_2)+'.'+ str(ft_info_type_ver_3) + '.' + str(ft_info_type_ver_4)+').hex', 'wb')
    fi.write(ft_ibody)
    fi.close()
