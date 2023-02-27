import socket
import threading

def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        pass
    s.close()

if __name__ == "__main__":
    host = input("Enter the IP address to scan: ")
    threads = []
    for port in range(1, 65536):
        t = threading.Thread(target=port_scan, args=(host, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
        
       
  # This script checks for open ports on a machine in range 1 - 65536 #

 # To run make sure latest version of python is installed then run script using powershell #

# Script will ask for ip to scan, enter your ip to see open ports #


# Example Output: 

Enter the IP address to scan: 202.61.134.138
Port 139 is open
Port 135 is open
Port 445 is open
Port 902 is open
Port 912 is open
Port 5040 is open
Port 5426 is open 
