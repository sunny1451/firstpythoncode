#Port Scanner

import socket

target_ip="127.0.0.1"
ports=[21,22,80,443]

for port in ports:
    s=socket.socket()
    result = s.connect_ex((target_ip,port))
    if result == 0:
        print(f"port{port} is open")
    s.close()                            #if port is open it shows 0
                                    #if any port is not opended there is no output displays
    
    
