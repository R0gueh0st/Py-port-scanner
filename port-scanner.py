#! /usr/bin/python


import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

# Ask for input
remoteServer =raw_input("Enter remote host IP to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Select ports to Scan
print("""
1. Default ports (1 - 1024)
2. Port 80
3. Port 443
4. Port 22
5. Port 3389
""")
port_selection = raw_input("Please select the ports you'd like to scan: ")

#Print a nice banner with host info
print "-" * 65
print "Please wait, scanning remote host", remoteServer + " - " + remoteServerIP
print "-" * 65

# Check what time the scan started
t1 = datetime.now()

print 'Scan started at ', t1

if port_selection == "1":
	try:
		for port in range(1,1025):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.10)
			result = sock.connect_ex((remoteServerIP, port))
			if result == 0:
				print "Port{}: Open".format(port)
			sock.close()
	except KeyboardInterrupt:
		print "You pressed Ctrl+C.  Aborting..."
		sys.exit()

	except socket.gaierror:
		print 'Hostname could not be resolved...exiting...'
		sys.exit()

	except socket.error:
		print "Couldn't connect to server"
		sys.exit()
elif port_selection == "2":
	ports = 80
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.10)
	result = sock.connect_ex((remoteServerIP, ports))
	if result == 0:
		print "Port{}: Open".format(ports)
	elif result != 0:
		print "Selected port(s) closed"
	sock.close()
elif port_selection == "3":
	ports = 443
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.10)
	result = sock.connect_ex((remoteServerIP, ports))
	if result == 0:
		print "Port{}: Open".format(ports)
	elif result != 0:
		print "Selected port(s) closed"
	sock.close()
elif port_selection == "4":
	ports = 22
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.10)
	result = sock.connect_ex((remoteServerIP, ports))
	if result == 0:
		print "Port{}: Open".format(ports)
	elif result != 0:
		print "Selected port(s) closed"
	sock.close()
elif port_selection == "5":
	ports = 3389
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.10)
	result = sock.connect_ex((remoteServerIP, ports))
	if result == 0:
		print "Port{}: Open".format(ports)
	elif result != 0:
		print "Selected port(s) closed"
	sock.close()
else:
	print ("Invalid selection... exiting")
	sys.exit()

# Check the time again
t2 = datetime.now()

# Scan completed time
print 'Scan completd at ', t2

# Calculates the difference of time, to see how long it took to run the scan
total = t2 - t1

# Print info to screen
print 'Scanning Completed in: ', total
