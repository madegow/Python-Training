#gettig ip adresses assignments

import netifaces
import scapy.all as scapy

g_way=netifaces.gateways()
print(g_way)

default=g_way[2][0][0]
print(default)

ip=default.split('.')[0:3]
print(ip)
ip1='.'.join(ip)
print(ip1)

for i in range(100, 255):
	ip = ip1+'.'+str(i)
	arp_frame = scapy.ARP(pdst=ip)
	broadcast_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	request_frame = broadcast_frame/arp_frame
	scan_result = scapy.srp(request_frame, timeout = 1, verbose = False)[0]
	result = list()
	for i in range(0, len(scan_result)):
		client_dict = {"ip" : scan_result[i][1].psrc, "mac" : scan_result[i][1].hwsrc}
		if bool(client_dict):
			result.append(client_dict)
			print(result)

print(ip)
interfaces = netifaces.interfaces()
print(interfaces)




