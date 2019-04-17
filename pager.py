import sys
import time
from scapy.all import IP, ICMP, send, Raw, sendp

num_send = 5
ref_ip_list = []
#dest_ip = "152.3.136.197"
ip_list_file = open(sys.argv[1],"r")
for eachline in ip_list_file:
    ref_ip_list.append(eachline.strip())
print (ref_ip_list)
while True:
  for ref_ip in ref_ip_list:
#  packet = IP(dst= ref_ip,src = dest_ip ) / ICMP()/  str(int(time.time()*1000))
    packet = IP(dst= ref_ip) / ICMP()/  str(int(time.time()*1000))
    for i in range(num_send):
      time.sleep(1)
      print ("send to ",ref_ip)
      send(packet)
