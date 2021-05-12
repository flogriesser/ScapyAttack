from scapy.all import *


# Wireshark filter: tcp.flags.ack==1 && tcp.flags.syn==1

packet = IP(dst="192.168.62.60", src="192.168.62.70") / TCP(dport=(1,100), flags="S")
sr(packet, inter=0.005) 
