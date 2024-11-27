"""AUFGABE:
Schreiben Sie ein Python-Programm, das aus einer Liste von IP-Adressen testet ob die IPs gültig sind und 
eine Funktion die nur die Adressen zurückgibt, die zu einem bestimmten Subnetz gehören.
"""

# split Array
# Anz Bloecke checken
# jeder Block soll numerisch sein und nicht <0 oder >255 
# durch gueltige IP-Liste iterieren und mit Subnetz vergleichen

import ipaddress
# ipaddress Modul validiert die Adresse bei der Funktion ip_adress(ip) bereits automatisch -> ValueError: '256.0.0.3' does not appear to be an IPv4 or IPv6 address

# Liste mit Bsp-IPv4-Adressen
list_of_ips = ["192.168.1.1", "123.123.123.3", "256.0.0.3", "128.129.130.131", "192.141.455.0", "255.255.255.255", "192.168.2.1", "10.0.0.1", "192.168.3.5"] 
subnet = "192.168.0.0/16"
# Um das Subnetz als ip_network zu definieren
netz = ipaddress.ip_network(subnet)

# Funktion Gueltigkeit
def is_valid_ipv4(ip):
    parts=ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True


for ip in list_of_ips:
    print(f"Die IP {ip} ist gültig: {is_valid_ipv4(ip)}")
  
valid_ips=[ip for ip in list_of_ips if is_valid_ipv4(ip)]
print("\nGültige IP-Adressen:", valid_ips)

for ip in valid_ips:
    if ipaddress.ip_address(ip) in netz:
        print("Die IP gehört zum Subnetz.")
    else:
        print("Die IP gehört nicht zum Subnetz.")