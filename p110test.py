from PyP100 import PyP110

p110 = PyP110.P110("192.168.1.33", "myemail", "mypass")

p110.handshake() #Creates the cookies required for further methods
p110.login() #Sends credentials to the plug and creates AES Key and IV for further methods


name=p110.getDeviceName() #Returns the name of the connected plug set in the app
info=p110.getDeviceInfo() #Returns dict with all the device info of the connected plug
state=p110.toggleState() #Toggles the state of the connected plug
#The P110 has all the same basic functions as the plugs and additionally allow for energy monitoring.
energy=p110.getEnergyUsage() #Returns dict with all of the energy usage of the connected plug

print("*******************************************************")
print("name", name)
print("-------------------------------------------------------")
print("info", info)
print("-------------------------------------------------------")
print("state", state)
print("-------------------------------------------------------")
print("energy", energy)
print("*******************************************************")