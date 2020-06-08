Computer has 4 main things
 CPU 
 Memory (RAM)
 Storage (Permanent)
 Network
 
Environmental Factors 
 Time
 Temp

 Displayed on the LED through Alexa

 Details:

 * IP address
 * Time
 * Up Time
 * Temperature
 * Disk free
 * CPU load
 * Memory free
 

 Ordered by difficulty

 Time
 Up Time
 Clock
 Disk free
 CPU load
 Memory free
 IP address
 Temperature
 Current Temperature
 


 Steps 1:

 one program for each.

 time.py
 uptime.py
 ...

 Step 2:

 system_info.py with argument 

 # python3 system_info.py get_ip

 <Show me ip address>

 # python3 sysmtem_info.py get_disk_free

 <show me disk free>

 ....

 how do you include other python files into one files

 Step 3:

 Web server

curl  http://<web address>/get_ip 
<IP address>

curl http://<web address>/

Step 4:

Alexa -> your web server

