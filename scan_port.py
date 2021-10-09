import socket

port_list = [80, 443, 8080]

open_networks = []

with open('scan_net.txt', 'r') as f:
    network_list = f.read().splitlines() 

for net in network_list:
   for port in port_list:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((net, port))

      if result == 0:
         open_networks.append(f"{net},{port}")
         print(f"{net} - {port} is open")
      sock.close()

with open('scan_net_working.txt', 'w') as f:
   f.writelines('\n'.join(open_networks))