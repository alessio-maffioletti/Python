import os

cmd = str((os.popen("ipconfig").read()).split())
ip = []
for index in range(0, len(cmd)):
    if cmd[index] == 'LAN':
        print(index)
        ip.append(cmd[index+1])
        
print(ip)