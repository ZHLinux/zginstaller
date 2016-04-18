#!/usr/bin/python
#-*-coding:utf-8-*-
import os

print "\n\t"
print "\n\t+-----------------------------------+"
print "\t|                                   |"
print "\t|         ZGinstaller v1.0          |"
print "\t|                                   |"
print "\t|    http://facebook.com/ZHLinux    |"
print "\t|                                   |"
print "\t+-----------------------------------+"
print "\n"


sel = raw_input("\033[1;36mPress enter key..... \033[1;m")

print "-------------------------------------------------------"

print "\n"

#commands -----------------------------------------------------------------------------------------------


print "\n"

os.system("reset && echo 'Your computer running is ' '\n\n' && uname -m")

bit=raw_input("\n\nBit : ")
if bit == "x86_64":
	os.system("wget http://files2.genymotion.com/genymotion/genymotion-2.6.0/genymotion-2.6.0-linux_x64.bin")
	print "\n\n------------------------------------------------------------------"
	print "\n"
	os.system("sudo apt-get install virtualbox")
	os.system("sudo apt-get install libgstreamer-plugins-base0.10-dev")
	print "\n\n------------------------------------------------------------------"
	os.system("chmod +x genymotion-2.6.0-linux_x64.bin")
	os.system("bash genymotion-2.6.0-linux_x64.bin")
	os.system("rm -r genymotion-2.6.0-linux_x64.bin")
	os.system("mv genymotion ~/.zgenymotion")
	os.system("ln -s ~/.zgenymotion/genymotion ~/Desktop/ZGenymotion")
	os.system("~/.zgenymotion/genymotion")
	
if bit == "i368":
	os.system("wget http://files2.genymotion.com/genymotion/genymotion-2.6.0/genymotion-2.6.0-linux_x86.bin")
	print "\n\n------------------------------------------------------------------"
	print "\n"
	os.system("sudo apt-get install virtualbox")
	os.system("sudo apt-get install libgstreamer-plugins-base0.10-dev")
	print "\n\n------------------------------------------------------------------"
	os.system("chmod +x genymotion-2.6.0-linux_x86.bin")
	os.system("bash genymotion-2.6.0-linux_x86.bin")
	os.system("rm -r genymotion-2.6.0-linux_x86.bin")
	os.system("mv genymotion ~/.zgenymotion")
	os.system("ln -s ~/.zgenymotion/genymotion ~/Desktop/ZGenymotion")
	os.system("~/.zgenymotion/genymotion")

#finish  -------------------------------------------------------------------------------------------------

#This program created by Zaur Hasanli
#Creator facebook adress : http://facebook.com/zaurhlee
#Creator youtube channel : https://www.youtube.com/channel/UCJCndfGlCt808IWlbG_liXw

#end     -------------------------------------------------------------------------------------------------

os.system("reset")

print "\n\t+---------------------------------------------------------------+"
print "\t|                                                               |"
print "\t|                     Creator by Zaur                           |"
print "\t|                                                               |"
print "\t|               http://facebook.com/ZHLinux                     |"
print "\t|                                                               |"
print "\t|   https://www.youtube.com/channel/UCJCndfGlCt808IWlbG_liXw    |"
print "\t|                                                               |"
print "\t+---------------------------------------------------------------+"
print "\n"
