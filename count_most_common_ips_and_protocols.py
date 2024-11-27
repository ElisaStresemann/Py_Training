import pyshark
from collections import Counter

# Lade und oeffne PCAP-Datei für Analyse
cap = pyshark.FileCapture('sectry.pcap')

# Test: Drucke das erste Paket
#for packet in cap:
#    print(packet)  
#    break  # Nur das erste Paket drucken, dann Abbruch

# Zaehler für IP-Adressen und Protokolle
# Counter-Objekt 
ipv4_counter = Counter()
ipv6_counter = Counter()
protocol_counter = Counter()

# Durchlaufe alle Pakete 
for packet in cap:
    # Zaehle IPs
    if 'IP' in packet:
        ipv4_counter[packet.ip.src]+=1
        ipv4_counter[packet.ip.dst]+=1
    #'IPv6' zaehlt zusaetzlich IPv6-Pakete
    elif 'IPv6' in packet:
        ipv6_counter[packet.ipv6.src]+=1
        ipv6_counter[packet.ipv6.dst]+=1

    # Zaehle Protokolle
    if 'IP' in packet:
        protocol_counter[packet.transport_layer]+=1


# Ausgabe haeufigste IP-Adresse - most_common() Methode aus Counter - ohne Parameter Auflistung der Haeufigkeiten in absteigender Reihenfolge
most_common_ipv4 = ipv4_counter.most_common(2)
print(most_common_ipv4)
print(f"Häufigste IPv4-Adresse: {most_common_ipv4[0][0]} mit {most_common_ipv4[0][1]} Paketen und {most_common_ipv4[1][0]} mit {most_common_ipv4[1][1]}")

most_common_ipv6 = ipv6_counter.most_common(1)
print(f"Häufigste IPv6-Adresse: {most_common_ipv6[0][0]} mit {most_common_ipv6[0][1]} Paketen")

# Ausgabeaeufigstes Protokoll
most_common_protocol = protocol_counter.most_common(1)
print(f"Haeufigstes Protokoll: {most_common_protocol[0][0]} mit {most_common_protocol[0][1]} Vorkommen")