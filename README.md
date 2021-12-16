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

A discussion of at least one major challenge, and how you overcame it:

- A major challenge that came up while we were working on our project was the runtime for the code. When we started testing our code to see if the port scanners were working properly and the program was doing everything we expected, we realized that scanning a port was taking too long. We wanted to scan 1024 ports, but we realized that with our runtime, it was not feasible. So we tested on 10 ports, and even that was taking a long time to run. We tested on one port at a time, but finding a port that was open and making sure that all different paths for our code worked was still a hassle. After talking to a couple of classmates, we realized that many of them were also encountering the same issue. We consulted with our classmates and made a plan to update one another if there were any advancements made regarding the issue. Soon enough, during one of the TA hour sessions, our classmates were able to show us this line of code: sock.settimeout(0.02) which made the process much faster and efficient. Because of this, we were able to test out all test cases to make sure our program ran fine and was scanning all ports. While this was a simple fix, it was a huge headache for us because just testing the code would have taken a lot of time, time that we could spend working on other parts of the project. Other than this obstacle, for other obstacles, we looked to our resources such as the internet, classmates, and instructors. 

Speficic contributions:

- Mariah White:

- Christina Sherpa:
