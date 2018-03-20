#coding=gdk
#get file in read and write 
FName = open("C:/Users/hyasn/Desktop/userinfo2.txt","a+")
#define a number to record number of name being read from file
userNum = 0
while str <> "":
	str = FName.readline()
	print(str)
	#while char = "\n":
		#userNum += 1
#print(userNum)
'''
#��ӡ4���û�
for i in range(0,4):
	str = ""
	char = ""
	while char <> "\n":
		char = FName.read(1)
		str = str + char
	print(str)
'''
FName.close()