import socket
from struct import unpack
from utils import mac_addr

class EthernetFrame:
    length = 14
    def __init__(self, data):
        unpacked_data = unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data[2])
        self.destination = mac_addr(data[0:6])
        self.source = mac_addr(data[6:12])
        self.leftover_data = data[self.length:]
    
    def __str__(self):
        return f"""
    EthernetFrame...
    * Source:           {self.source}
    * Destination:      {self.destination}
    * Protocol:         {self.protocol}
"""
    
class IPHeader:
    length = 20
    def __init__(self, data):
        unpacked_data = unpack('!BBHHHBBH4s4s', data[0:self.length]) 
        self.version = data[0] >> 4
        self.header_length = (data[0] & 15) * 4
        self.ttl = unpacked_data[3]
        self.protocol = unpacked_data[6]
        self.source_addr = socket.inet_ntoa(unpacked_data[8])
        self.dest_addr = socket.inet_ntoa(unpacked_data[9])
        self.leftover_data = data[self.length:]

    def __str__(self):
        return f"""
    IP Header...
    * Source Address:       {self.source_addr}
    * Destination Address:  {self.dest_addr} 
    * Protocol Version:     {self.version}
"""