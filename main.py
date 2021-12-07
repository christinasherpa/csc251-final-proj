#main file for storing all code 


# CSC 251 Final Project 
# Authors: Christina Sherpa and Mariah White 

import socket
from datetime import *
import os

##
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Input website to scan: ')

#will go into Scanner class
def npscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(1024):
    if npscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')

##

import socket
from datetime import *
import os

#checking if IP is alive
def main():
    user_ip = input("Please input an IP Adress: ")
    ret = os.system("ping -o -c 3 -W 3000 " + user_ip)
    if ret != 0:
        print("IP is alive...proceeding. ")
        #probe_ports(user_ip, 65535)
        #probe_ports(user_ip, 1024)

        probe_ports(user_ip, 10) #for test run
    else:
        print("IP is not alive, please try again. ")



def probe_ports(user_ip, x):
    start_clock = datetime.now()
    open_count = 0
    close_count = 0

    if x==1024:
        print("Probing only well known TCP ports")
    else:
        print("Probing all 2^16 TCP ports on a targeted host")

    remoteServerIP = user_ip 

    if(ord_choice=="seq"):
        #probing all ports in order
        for port in range(x):  
            remoteServerIP = "192.168.1.30"
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

    if(ord_choice=="seq"):
        #Probing ports in random orde
        lst = list(range(x))
        random.seed
        l1 = random.sample(lst, len(lst))

        for port in range(x):  
            remoteServerIP = "192.168.1.30"
            
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



main()











