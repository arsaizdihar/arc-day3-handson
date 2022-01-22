import socket as socklib

message = input("msg: ")
target = input("to: ")
targetIPs = {"ken": "10.147.18.138", "ditra": "10.147.18.202",
             "johannes": "10.147.18.114", "samuel": "10.147.18.1", "arsa": "10.147.18.42"}
targetPort = 9993
mysocket = socklib.socket(socklib.AF_INET, socklib.SOCK_DGRAM)

if target in targetIPs:
    targetIP = targetIPs[target]
    mysocket.sendto(message.encode(), (targetIP, targetPort))
else:
    for targetIP in targetIPs.values():
        mysocket.sendto(message.encode(), (targetIP, targetPort))
