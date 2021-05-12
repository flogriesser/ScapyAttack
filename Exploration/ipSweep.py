from scapy.all import *

# Wiresharkfilter: arp.opcode == 2

packet = IP(dst="192.168.62.0/24") / ICMP() / "1234567890"
send(packet, inter=0.005)
