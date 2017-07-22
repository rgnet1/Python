import sys

username = ["Google", "Pirates", "Doctor", "Walter White"]
passwd = [412, 123, 1, 5]
print("Enter your username (Case sensative)")
usr = sys.stdin.readline()
usr = usr.strip('\n')
pas = int(input("Enter your password: "))
i = 0
while i<len(username):
	while i<len(username):
		if username[i] == usr and passwd[i] == pas:
			print(username[i] +", You have successfully logged in")
			sys.exit()
		else:
			i+=1
i = 0
while i<len(username):
	if username[i] != usr or passwd[i] != pas:
		print("Log-in unseccessful... try again")
		break
	i+=1
