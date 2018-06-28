import paramiko

#              showIpInt.py
# This is a simple program that ssh's into Networkig devices and
# gets the interface configuration. This program requires all devices'
# ssh information reside in the file "config.txt", which should be in the
# same directory as this script.
#
# This program assumes devices are already set up for ssh (instructions
# can be found in the file "sshSetupCisco.txt"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Read in file for address, username and password
deviceList =[]
numOfDevices = 0
readfile = open("config.txt","r")
for line in readfile:
	line = line.strip("\r\n")
	line = line.split(" ")
	deviceList.append(line[0],line[1],line[2])
	numOfDevices +=1



for i in range(numOfDevices):
	print "********** Now Going into device: ",deviceList[i][1],"************"
	ssh.connect(deviceList[i][0],port=22, username=deviceList[i][1],
             	password=deviceList[i][2])

	#Now we can execute commands
	stdin, stdout, stderr = ssh.exec_command('show ip int brief')
	output = stdout.readlines()

	#print the output
	print '\n'.join(output)

