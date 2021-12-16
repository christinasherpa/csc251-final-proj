# csc251-final-proj
CSC 251 Final Project 
Authors: Christina Sherpa and Mariah White 


How to run our file (port_scanner.py):

command line usage:
- python port_scanner.py -ports[all/known] - order[random/seq] -scan_type[normal/syn/fin] -target_ip

How the code runs: 
- The code first checks if IP is alive or not. If it is alive, th following steps take place. 
- The code first runs the type of specific scan (normal scanning, TCP SYN scanning, or TCP FIN scanning)
- If those options aren't chosen, it runs all the scan types in random order 
- Next, it runs probes all or known ports in either random or seqeuntial order 
- When it runs, it gives the ports that are open or close and keeps a count as well. It also keep count of time. 

