#main file for storing all code 


# CSC 251 Final Project 
# Authors: Christina Sherpa and Mariah White 

import socket
from datetime import *
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Input website to scan: ')

def npscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        print('Port',x,'is closed')
        return False


for x in range(1024):
    if npscan(x):
        print('Port',x,'is open')


def main(SOMEHOST):

    SOMEHOST = "192.168.1.30"

    ret = os.system("ping -o -c 3 -W 3000 " + SOMEHOST)
    if ret != 0:
        print("IP is alive...proceeding. ")
        probe(65535)
        probe(1024)
    else:
        print("IP is not alove, please try again. ")



def probe(x):
    start_clock = datetime.now()
    open_count = 0
    close_count = 0

    if x==1024:
        print("Probing only well known TCP ports")
    else:
        print("Probing all 2^16 TCP ports on a targeted host")


    #probing all ports in order
    for port in range(x):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port)) #printing what ports are open 
            open_count = open_count +1 
        else:
            print("Port {}: Close".format(port)) #printing what ports are open 
            close_count = close_count +1 
        sock.close()
    print("Probing ports in order...")
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {}".format(close_count))

    #Probing ports in random orde
    lst = list(range(x))
    random.seed
    l1 = random.sample(lst, len(lst))

    for port in range(x):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port)) #printing what ports are open 
            open_count = open_count +1 
        else:
            print("Port {}: Close".format(port)) #printing what ports are open 
            close_count = close_count +1 
        sock.close()
    print("Probing ports in random order...")
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {}".format(close_count))
    end_clock = datetime.now()
    time = end_clock-start_clock
    print("Scan done! IP address (1 Host up) done in {} seconds.".format(time))







