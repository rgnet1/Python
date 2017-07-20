
#This is my python replication of my String Sorter from java
# As you can see,there is much less code used in python
import sys

class StringSet:
	__n = "Try again"
	__str1 = ""
	__str2 = ""
	__str3 = ""
	__temp = []
	def __init__(self, str1, str2, str3):
		self.__str1 = str1
		self.__str2 = str2
		self.__str3 = str3
		self.__temp = [str1, str2, str3]
		self.__temp.sort()

	def getSmallest(self):
		return self.__temp[0]

	def getLargest(self):
		return self.__temp[2]

	def getMiddle(self):
		return self.__temp[1]

	def getList(self):
		return self.__temp

print("Please enter a word")
str1 = sys.stdin.readline()
str1 = str1.replace('\n', '') #I could use .strip('\n') instead
print("Please enter a word")
str2 = sys.stdin.readline()
str2 = str2.replace('\n', '')
print("Please enter a word")
str3 = sys.stdin.readline()
str3 = str3.replace('\n', '')

stringList = StringSet(str1, str2, str3)

print("Smallest is ", stringList.getSmallest())
print("The entire List is ", stringList.getList())

