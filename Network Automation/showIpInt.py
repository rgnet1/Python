import paramiko
import time

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



def readFile(fileName):
	deviceList =[]
	numOfDevices = 0
	readfile = open("config.txt","r")
	for line in readfile:
		line = line.strip("\r\n")
		line = line.split(" ")
		deviceList.append([line[0],line[1],line[2]])
		numOfDevices +=1

	return numOfDevices,deviceList


def execute_commands(ip_commands, ssh_remote, device_name):
	command_list = open(ip_commands, 'r')

	
	for line in command_list:
		new_file = 'output-'+ device_name + '.txt'
		result = open(new_file, 'w+')
		cmd = line.strip()
		if len(cmd) > 0:
			title = 'About to execute command: ' + cmd
			top_bar = '           '

			for z in range(0, len(title), 1):
				top_bar += '_'
			print top_bar

			curr_cmd = '__________|About to execute command: ' + line.strip() + '|__________'
			print curr_cmd

			empty_line = '|'
			for y in range(0, len(curr_cmd)-1,1):
				empty_line +=' '
			empty_line += '|'
			print empty_line

			#Now we can execute commands
			ssh_remote.send(line.lstrip())

			time.sleep(1)
			output = ssh_remote.recv(655350)
			success_string = '| command status: successful'
			invalid_string = '| command status: invalid'
			if 'Invalid input' in output or 'Incomplete command' in output:
				for u in range(0,len(curr_cmd) - len(invalid_string), 1):
					invalid_string += ' '
				invalid_string += '|'
				print invalid_string
			else:
				for u in range(0,len(curr_cmd) - len(success_string), 1):
					success_string += ' '
				success_string += '|'
				print success_string

			end_line = '|'
			for x in range(0, len(curr_cmd)-1,1):
				end_line += '_'
			end_line += '|\n\n\n'
			print end_line

			result.write(output + '\n')
			result.close()

		



#Read in file for address, username and password
numOfDevices, deviceList = readFile("config.txt")


for i in range(numOfDevices):
	print "********** Now Going into device: ",deviceList[i][0]," ************"
	ssh.connect(deviceList[i][0],port=22, username=deviceList[i][1],
             	password=deviceList[i][2])

	ssh_remote = ssh.invoke_shell()

	execute_commands(deviceList[i][0], ssh_remote, deviceList[i][0])
	
	ssh.close()
	#Now we can execute commands
	# stdin, stdout, stderr = ssh.exec_command('show version')
	# output = stdout.readlines()

	#print the output

