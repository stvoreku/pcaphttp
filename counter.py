import pyshark
import sys

# try:
#     file_path = sys.argv[1]
# except:
#     print('Provide path to pcap file!')
#     sys.exit(1)

file_path = 'file.pcap'
file_path = 'file_new.pcap'

file = pyshark.FileCapture(file_path)
print(f'GOT: {file_path}, \n PARSING...')

connections = {}

for p in file:
    try:
        conn = f'{p.ip.src}:{p.ip.dst}'
        if conn not in connections.keys():
            connections[conn] = 1
        else:
            connections[conn] += 1
    except:
        pass


connections_temp = sorted(connections.items(), key=lambda x:x[1], reverse=True)
connections_sorted = dict(connections_temp)

print(connections_sorted)
