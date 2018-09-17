import paramiko
import time
import argparse
# used for running os commands
import pexpect

#              showIpInt.py
# This is a simple program that ssh's into Networkig devices and
# gets the interface configuration. This program requires all devices'
# ssh information reside in the file "config.txt", which should be in the
# same directory as this script.
#
# This program assumes devices are already set up for ssh (instructions
# can be found in the file "sshSetupCisco.txt"


parser = argparse.ArgumentParser()
parser.add_argument('-kfile', '--kevinfile')
parser.add_argument('-sf', '--singlefile')

args = parser.parse_args()
kevin_file = args.kevinfile
single_file = args.singlefile

kevin_flag = False
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

config_mode = {
        'cisco': 'en\nconf t\ntermlen 0',
        'juniper': 'cli\nconfigure\nset cli screen-length 0'

    }


def readFile(fileName):
	deviceList =[]
	numOfDevices = 0
	readfile = open("log in credentials.txt", "r")
	for line in readfile:
		# Skip commented out
		if not line.startswith('#') and not line.startswith('//'):
			line = line.strip("\r\n")
			line = line.split(" ")
			deviceList.append([line[0], line[1], line[2]])
			numOfDevices += 1

	return numOfDevices, deviceList


def print_progress(line):
	title = 'About to execute command: ' + cmd
	top_bar = '           '

	for z in range(0, len(title), 1):
		top_bar += '_'
	print top_bar

	curr_cmd = '__________|About to execute command: ' + line.strip() + '|__________'
	print curr_cmd

	empty_line = '|'
	for y in range(0, len(curr_cmd) - 1, 1):
		empty_line += ' '
	empty_line += '|'
	print empty_line

	return curr_cmd


def print_cmd_completion_status(curr_cmd, output):
	success_string = '| command status: successful'
	invalid_string = '| command status: invalid/incomplete'
	if 'Invalid input' in output or 'Incomplete command' in output:
		for u in range(0, len(curr_cmd) - len(invalid_string), 1):
			invalid_string += ' '
		invalid_string += '|'
		print invalid_string
	else:
		for u in range(0, len(curr_cmd) - len(success_string), 1):
			success_string += ' '
		success_string += '|'
		print success_string

	end_line = '|'
	for x in range(0, len(curr_cmd) - 1, 1):
		end_line += '_'
	end_line += '|\n\n\n'
	print end_line
# DEFUALT COMMANDS I NEED TO IMPLEMENT:
# enable, conf t, terminal len 0
def execute_commands(ip_commands, ssh_remote, device_name, kevin_flag, k_file_name):
	if kevin_flag:
		print 'Kevin flag is on'
		global begin_found
		global start
		command_list = open(ip_commands, 'w')
		kevin_file = open(k_file_name, 'r')
		command_list.write('enable\n')
		command_list.write('conf t\n')
		command_list.write('terminal len 0\n')
		for line in kevin_file:
			while begin_found <= start:
				if line.startswith('######') and 'BEGIN CONFIG' in line:
					begin_found += 1
				else:
					command_list.write(line.strip() + '\n')
					print 'Writing the following cmd: ['+ line.strip()+']'

				line = kevin_file.next()
		command_list.close()
		start = begin_found
		exit()
	new_file = 'output-' + device_name + '.txt'
	result = open(new_file, 'w')
	command_list = open(ip_commands, 'r')
	for line in command_list:

		cmd = line.strip()
		if len(cmd) > 0 and '!' != cmd:
			curr_cmd = print_progress(line)

			# Now we can execute commands
			ssh_remote.send(line.lstrip())
			if 'show run' in line:
				time.sleep(5)
			else:
				time.sleep(1)

			output = ssh_remote.recv(655350)
			print_cmd_completion_status(curr_cmd, output)

			result.write(output + '\n')
	result.close()
	return new_file

		


# Main()

#Read in file for address, username and password
numOfDevices, deviceList = readFile("log in credentials.txt")

if kevin_file:
	global begin_found
	global start
	start = 0
	begin_found = 0
	kevin_flag = True
	print 'KEVIN FILE'
output_files_list = []


for i in range(numOfDevices):
	print "********** Now Going into device: ", deviceList[i][0], " ************"
	ssh.connect(deviceList[i][0], port=22, username=deviceList[i][1], password=deviceList[i][2])

	ssh_remote = ssh.invoke_shell()

	if single_file:
		output_file = execute_commands(single_file, ssh_remote, deviceList[i][0], kevin_flag, kevin_file)
	else:
		output_file = execute_commands(deviceList[i][0], ssh_remote, deviceList[i][0], kevin_flag, kevin_file)
	
	ssh.close()

	output_files_list.append(output_file)

print '\n\n            Checking for errors'

# Check for errors or invalid input
for z in range(0, len(output_files_list), 1):
	title = output_files_list[i].strip('output-')
	title = title.strip('.txt')

	print 'Device ' + title + ' Errors'

	process = pexpect.spawn('cat ' + output_files_list[i] + ' grep -B 2 Invalid')

	print process.before
	process.interact()
