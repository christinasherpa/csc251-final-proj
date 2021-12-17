# csc251-final-proj
CSC 251 Final Project 
Authors: Christina Sherpa and Mariah White 


How to run our file (port_scanner.py):

command line usage:
- python port_scanner.py -ports[all/known] - order[random/seq] -scan_type[normal/syn/fin] -target_ip

How the code runs: 
- The code first checks if IP is alive or not. If it is alive, th following steps take place. 
- The code first runs the type of specific scan (normal scanning, TCP SYN scanning, or TCP FIN scanning)
- For these scans, you can change the IPs and range of ports manually. We did not include this in the command line because we didnt want to overwhelm our users. 
- If those options aren't chosen, it runs all the scan types in random order 
- Next, it runs probes all or known ports in either random or seqeuntial order 
- When it runs, it gives the ports that are open or close and keeps a count as well. It also keep count of time. 

A discussion of at least one major challenge, and how you overcame it:

- A major challenge that came up while we were working on our project was the runtime for the code. When we started testing our code to see if the port scanners were working properly and the program was doing everything we expected, we realized that scanning a port was taking too long. We wanted to scan 1024 ports, but we realized that with our runtime, it was not feasible. So we tested on 10 ports, and even that was taking a long time to run. We tested on one port at a time, but finding a port that was open and making sure that all different paths for our code worked was still a hassle. After talking to a couple of classmates, we realized that many of them were also encountering the same issue. We consulted with our classmates and made a plan to update one another if there were any advancements made regarding the issue. Soon enough, during one of the TA hour sessions, our classmates were able to show us this line of code: sock.settimeout(0.02) which made the process much faster and efficient. Because of this, we were able to test out all test cases to make sure our program ran fine and was scanning all ports. While this was a simple fix, it was a huge headache for us because just testing the code would have taken a lot of time, time that we could spend working on other parts of the project. Other than this obstacle, for other obstacles, we looked to our resources such as the internet, classmates, and instructors. 

Speficic contributions:

- Mariah White: worked on implementing the three distinct port types: normal port scan, tcp syn scan and tcp fin scan. Within the port scan, the main module used was socket. A client connection had to be created for each port. We were able to distinguish which ports were closed and open through print statements. Scapy was needed for the tcp syn and tcp fin scan which were similar in structure though each had different flag values set, signifying the type of scan. We decided to do away with classes for each port which was our initial idea, and left them inside their own functions.


- Christina Sherpa: worked on the second portion of the project which was testing the life of the inputted ip, configuring probe functions for both sequential and random order, and determining how our code would display in the command line. The main tools used for these implementations were random, datetime and os modules. Ping was utilized to see if the ip is alive, which was true when our ret variable equals 0. For the random probe specifically, we had to make sure there wasn’t repetition of any one port scanned. This required a little more effort than probing in order. Within the command line, four arguments had to be set, determining the user’s preferences for the scan. These were the number of ports to be scanned, order, target ip and scan type. In displaying the results, a count was set to keep track of each individual closed and open port. There also had to be a way to record how long the scan took which was done using the datetime module, subtracting end time from start time. We had to then merge our three scan implementations with the working probe functions and make sure it seamlessly functioned in the command line as it should. 

Citations:
- https://www.geeksforgeeks.org/port-scanner-using-python/
- https://www.oreilly.com/library/view/python-penetration-testing/9781789138962/9f389f41-4489-4628-a61f-969eea3aae8c.xhtml
- https://www.meridianoutpost.com/resources/articles/well-known-tcpip-ports.php
- https://medium.com/@avirj/nmap-tcp-syn-scan-50106f818bf1
- https://pretagteam.com/question/python-check-if-ip-is-up-or-down
- https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments
- https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/
- https://osqa-ask.wireshark.org/questions/7896/number-of-open-ports/

