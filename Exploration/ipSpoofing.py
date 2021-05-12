from scapy.all import *



packet = IP(dst="192.168.62.0/24", src="192.168.62.80") / ICMP() /"1234567890" 
sr(packet, inter=0.005) 
