import pyshark
from collections import Counter

# Lade und öffne PCAP-Datei für Analyse
cap = pyshark.FileCapture('sectry.pcap')

# Test: Drucke das erste Paket
#for packet in cap:
#    print(packet)  
#    break  # Nur das erste Paket drucken, dann Abbruch

# Zähler für IP-Adressen und Protokolle
ip_counter = Counter()
protocol_counter = Counter()

# Durchlaufe alle Pakete 
for packet in cap:
    # Zähle IPs
    if 'IP' in packet:
        ip_counter[packet.ip.src]+=1
        ip_counter[packet.ip.dst]+=1

    # Zähle Protokolle
    if 'IP' in packet:
        protocol_counter[packet.transport_layer]+=1


# Ausgabe häufigste IP-Adresse
most_common_ip = ip_counter.most_common(1)
print(f"Häufigste IP-Adresse: {most_common_ip[0][0]} mit {most_common_ip[0][1]} Paketen")

# Ausgabeäufigstes Protokoll
most_common_protocol = protocol_counter.most_common(1)
print(f"Häufigstes Protokoll: {most_common_protocol[0][0]} mit {most_common_protocol[0][1]} Vorkommen")