from scapy.all import *

Run = True

while Run:
    print('What packet would you like to send?')
    print('0: SYN & FIN\n1: FIN\n2: URG\n3: No Flag\nq: Exit')

    input_value = input('Enter command:')

    if input_value == '0':
        print("SYN & FIN\n")
        packet = IP(dst="192.168.62.60") / TCP(flags="SF")
        send(packet, count = 10, inter=0.05) 
        
    if input_value == '1':
        print("FIN\n")
        packet = IP(dst="192.168.62.60") / TCP(flags="F")
        #sr(packet) 
        send(packet, count = 10, inter=0.05) 
    
    if input_value == '2':
        print("URG (dport is for Netbios)\n")
        packet = IP(dst="192.168.62.60") / TCP(flags="U", dport=139)
        sr(packet) 
        #send(packet, count = 10, inter=0.05) 

    if input_value == '3':
        print("No Flag\n")
        packet = IP(dst="192.168.62.60") / TCP(flags="")
        #sr(packet)
        send(packet, count = 10, inter=0.05) 
    
    if input_value == 'q':
        Run = False