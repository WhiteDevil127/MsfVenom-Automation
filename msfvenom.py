import subprocess
import ownmodule

name = "                       MSFVenom"
name2 = "                            Automation"


print("------------------------------------------------------------------------------------------------------------")

subprocess.call(["figlet", "-f", "big", name])
subprocess.call(["figlet", "-f", "small", name2])

print("------------------------------------------------------------------------------------------------------------")

print("                                  Created By WhiteDevil")
print("                                  Our Youtube Channel")
print("                      https://www.youtube.com/channel/UCGuhWHXIhobET_RYILoj6fQ")
print("                                  Subscribe For More Updates")

payload = input("Enter Payload: ")

while payload == "":
   print("Enter Valid Payload")
   payload = input("Enter Payload: ")


LHOST = input("Enter LHOST: ")

while LHOST == "":
   print("Enter Valid LHOST")
   LHOST = input("Enter LHOST: ")

LPORT = input("Enter LPORT: ")

while LPORT == "":
   print("Enter Valid LPORT")
   LPORT = input("Enter LPORT: ")
   
fname = input("Enter Your File Name: ")

while fname == "":
   print("Enter Valid File Name")
   fname = input("Enter Your File Name: ")

ownmodule.generate(payload, LHOST, LPORT, fname)


