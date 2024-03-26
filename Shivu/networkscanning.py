import netifaces
import scapy.all as scapy
import nmap

print("Starting ...")

class nvpt:
	def __init__(self, d_gatewaytmp="192.168.0.1"):
		self.d_gateway = d_gatewaytmp
		self.result = list()
		
	def scannetwork(self):
		octet_list3 = self.d_gateway.split('.')[0:3]
		ip_string = '.'.join(octet_list3)
	
		for last_octet in range(100,254):
			ip = ip_string+'.'+str(last_octet)
			arp_frame = scapy.ARP(pdst=ip)
			broadcast_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
			request_frame = broadcast_frame/arp_frame
			scan_result = scapy.srp(request_frame, timeout = 1, verbose = False)[0]
			for i in range(0, len(scan_result)):
				client_dict = {"ip" : scan_result[i][1].psrc, "mac" : scan_result[i][1].hwsrc}
				if bool(client_dict):
					self.result.append(client_dict['ip'])
		return self.result
	
	def scanmachine(self):
		if not self.result:
			self.scannetwork()
		for ip in self.result:
			print(ip)
			scanner = nmap.PortScanner()
			scanner.scan(ip, arguments='-sS -O')
			print(scanner.all_hosts())
			for host in scanner.all_hosts():
				print(host)
			#for port in scanner[host]['tcp'].keys():
			#	print('Port %s is %s' % (port, scanner[host]['tcp'][port]['state']))
			




if __name__ == "__main__":
   """
   nwlist = netifaces.gateways()
   NW = networks(str(nwlist['default'][netifaces.AF_INET][0]))
   """
   nwlist = netifaces.interfaces()
   gateways = netifaces.gateways()
   default_gateway=gateways[2][0][0]
   print(default_gateway)
   net = nvpt()
   net.scannetwork()
   net.scanmachine()
   exit(0)

	

