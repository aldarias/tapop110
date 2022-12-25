from PyP100 import PyP110


ips = ["33","34","35","36"]

for i in ips:

    ip =  '192.168.1.'+i
    p110 = PyP110.P110("192.168.1.33", "myemail", "mypass")
    p110.handshake() #Creates the cookies required for further methods
    p110.login() #Sends credentials to the plug and creates AES Key and IV for further methods

    print("*******************************************************")
   
    name=p110.getDeviceName() #Returns the name of the connected plug set in the app
    print("name", name)

    print("-------------------------------------------------------")
    info=p110.getDeviceInfo() #Returns dict with all the device info of the connected plug
    print("info", info)

    print("-------------------------------------------------------")

    #The P110 has all the same basic functions as the plugs and additionally allow for energy monitoring.
    energy=p110.getEnergyUsage() #Returns dict with all of the energy usage of the connected plug
    print("energy", energy)

    print("*******************************************************")
