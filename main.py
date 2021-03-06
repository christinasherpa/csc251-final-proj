# CSC 251 Final Project 
# Authors: Christina Sherpa and Mariah White 


import sys
import socket
from datetime import *
import os
import random
import scapy


def main():

    #getting args from the command line 
    ports= sys.argv[1] 
    if ports == "all":
        num_ports= 65535
    elif ports == "known":
        num_ports = 1024
    order= sys.argv[2] #this is either random or seq 
    target_ip = sys.argv[3] #IP that the user wants to use 

    scan_type = sys.argv[4] #have the options be "all" or a apecific scan 
    
    #checks if IP is alive or not 
    ret = os.system("ping -o -c 3 -W 3000 " + target_ip)
    #print(ret)
    if ret == 0:
        print("IP is alive...proceeding. ")


        #implement 3 modes of scanning here 

        if scan_type == "normal": #normal port scanning 
            #normal_scanning(x, target_ip)
            print("normal")
        elif scan_type == "syn":
            #syn_scanning()
            print("syn")
        elif scan_type == "fin":
            #fin_scanning()
            print("fin")
        else:
            lst = list(range(3))
            random.seed
            l1 = random.sample(lst, len(lst))

            for a in l1:
                if a==0:
                    #normal_scanning(x, target_ip)
                    print("Normal")
                elif a==1:
                    print("fin")
                    #fin_scanning()
                elif a==2:
                    print("syn")
                    #syn_scanning()


        #probing all/known ports
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
            #print("Port {}/{}: Close".format(port, service))  #printing what ports are closed
            close_count = close_count +1 
        sock.close()
    
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {}".format(close_count))
    end_clock = datetime.now()
    time = end_clock-start_clock
    print("Scan done! IP address ({} host up) scanned in {} seconds.".format(open_count,time))


def normal_scanning(x, target_ip):
    print("Normal Port Scanning")
    
    open_count = 0
    close_count = 0
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
            #print("Port {}/ {}: Close".format(port, service))  #printing what ports are closed
            close_count = close_count +1 

        sock.close()
        
    print("Number of open ports: {}".format(open_count))
    print("Number of closed ports: {} ".format(close_count))
    end_clock = datetime.now()
    time = end_clock-start_clock
    print("Normal scannign done! IP address ({} Host up) scanned in {} seconds.\n\n\n".format(open_count, time))

def fin_scan(x, target_ip):
    #change src to your local IP and dport range to a range you wish 
    print("TCP FIN Scanning")
    dst = target_ip
    ip_info = IP(src="131.229.238.101", dst ="132.229.72.13")
    tcp_info = TCP(sport =1024, dport=range(1,10), flags="F", seq=12345)
    packets = ip_info/tcp_info
    p = sr(packets)
    p.show()

def syn_scan(x, target_ip):
    print("TCP SYN Scanning")
    ip_info = IP(dst="132.229.72.13")
    tcp_info = TCP(sport=123,dport=(20,25),flags="S")
    packets = ip_info/tcp_info
    p = sr(packets)
    p.show()

main()



#dont show closed ports 
