import socket
import uuid

#get the hostname 
hostname = socket.gethostname()
# get the id id_address
id_address = socket.gethostbyname(hostname)

print(f"IP Address: {id_address}")

# Get the Mac Address
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                        for elements in range(0, 2*6, 8)][::-1])
print(f"MAC Address: {mac_address}")
