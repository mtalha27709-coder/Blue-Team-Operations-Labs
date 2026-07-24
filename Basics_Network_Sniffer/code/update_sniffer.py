from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        print(f"""
Source IP: {packet[IP].src}
Destination IP: {packet[IP].dst}
Protocol: {packet[IP].proto}
Packet Length: {len(packet)}
---------------------------
""")

print("Sniffing packets...\n")

sniff(prn=packet_callback, count=15)


