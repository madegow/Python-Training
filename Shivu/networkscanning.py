from uu import Error
import netifaces
import scapy.all as scapy


print("Starting ...")

class nvpt:
	def __init__(self, d_gatewaytmp="192.168.0.1"):
		self.d_gateway = d_gatewaytmp
		self.result = list()
		
		
	def scannetwork(self):
		ip=self.d_gateway
		first_three_octet = ip.split('.')[:3]
		ip_string = '.'.join(first_three_octet)
		ip_t = ip_string+'.'+'0'+'/24'
		print(ip_t, type(ip_t))
		arp_frame = scapy.ARP(pdst=ip_t)
		broadcast_frame = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
		request_frame = broadcast_frame/arp_frame
		print(request_frame)
		answered = scapy.srp(request_frame, timeout = 5, verbose = True)[0]
		print("Ansered =====", answered.summary())
		
		exit()
		first_three_octet = ip.split('.')[:3]
		ip_string = '.'.join(first_three_octet)
		print(ip_string)
		for i in range(100,254):
			try:
				ip_t = ip_string+'.'+str(i)
				print(ip_t, type(ip_t))
				arp_frame = scapy.ARP(pdst=ip_t)
				broadcast_frame = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
				request_frame = broadcast_frame/arp_frame
				print(request_frame)
				answered, unanswered = scapy.srp(request_frame, timeout = 5, verbose = True)[0]
				print("Ansered =====", answered.summary())
				print("UnAnsered =====", unanswered.summary())
			except:
				print(i, Error)
				
			
		exit(0)
		arp_frame = scapy.ARP(pdst=ip)
		broadcast_frame = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
		request_frame = broadcast_frame/arp_frame
		
		answered, unanswered = scapy.srp(request_frame, timeout = 5, verbose = False)[0]
		print("Ansered =====", answered.summary())
		print("UnAnsered =====", unanswered.summary())

		my_lambda = lambda s,r: self.result.append(r['ARP'].psrc)
		answered.filter(my_lambda)
		print(type(self.result))
		print(self.result.remove(self.d_gateway))
		self.result.remove("192.168.0.108")
		return self.result
	
	def portscan(self):
		for ip in self.result:
			print(ip)
			ans = scapy.sr1(scapy.IP(dst=ip)/scapy.ICMP(), timeout=2)
			print(type(ans))
			if len(ans) == 0:
				print(ip+": not pinging")
			else:
				print(ip+": successful in pinging")


		
def get_gateway():
	routes=	scapy.conf.route.routes
	# Find the default gateway
	for route in routes:
		if route[0] == 0 and route[1] == 0:
			return route[2]
	return None


if __name__ == "__main__":
   """
   nwlist = netifaces.gateways()
   NW = networks(str(nwlist['default'][netifaces.AF_INET][0]))
   """
   #gateways = netifaces.gateways()
   default_gateway=get_gateway()
   #print(default_gateway)
   net = nvpt(default_gateway)
   net.scannetwork()
   net.portscan()
   exit(0)
