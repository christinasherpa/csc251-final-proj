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


def main():

    #getting args from the command line 
    
    ports= sys.argv[1] 
    if ports == "all":
        num_ports= 65535
    elif ports == "known":
        num_ports = 1024
    order= sys.argv[2] 
    target_ip = sys.argv[3] 

    #user_ip = "131.229.72.13"
    ret = os.system("ping -o -c 3 -W 3000 " + target_ip)
    print(ret)
    if ret == 0:
        print("IP is alive...proceeding. ")
        if order == "random":
            probe_rand(target_ip, 10)
        elif order == "seq":
            probe(target_ip, 10) #for test run
    else:
        print("IP is not alive, please try again. ")
        

  

def probe(target_ip, x):
    open_count = 0
    close_count = 0

    if x==1024:
        print("Probing only well known TCP ports")
    else:
        print("Probing all 2^16 TCP ports on a targeted host")


    print("Probing ports in order...")
        #probing all ports in order
    for port in range(x):  
        start_clock = datetime.now()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.02)
        result = sock.connect_ex((target_ip, port))

        try:
            service = socket.getservbyport(port) 
        except OSError:
            service  = "Unknown"


        if result == 0:
            print("Port {}/ {}: Open".format(port, service)) #printing what ports are open 
            open_count = open_count +1 
        else:
            print("Port {}/ {}: Close".format(port, service))  #printing what ports are closed
            close_count = close_count +1 

        
        sock.close()
    
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {} ".format(close_count))
    end_clock = datetime.now()
    time = end_clock-start_clock
    print("Scan done! IP address ({} Host up) scanned in {} seconds.\n".format(open_count, time))


def probe_rand(target_ip, x):
    print("Probing ports in random order...")
    
    open_count = 0
    close_count = 0
        #Probing ports in random order
    lst = list(range(x))
    random.seed
    l1 = random.sample(lst, len(lst))

    for port in l1:  
        start_clock = datetime.now()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.02)
        result = sock.connect_ex((target_ip, port))

    
        try:
            service = socket.getservbyport(port) 
        except OSError:
            service  = "Unknown"


        if result == 0:
            print("Port {}/ {}: Open".format(port, service)) #printing what ports are open 
            open_count = open_count +1 
        else:
            print("Port {}/{}: Close".format(port, service))  #printing what ports are closed
            close_count = close_count +1 
        sock.close()
    
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {}".format(close_count))
    end_clock = datetime.now()
    time = end_clock-start_clock
    print("Scan done! IP address ({} host up) scanned in {} seconds.".format(open_count,time))



main()



#dont show closed ports 
