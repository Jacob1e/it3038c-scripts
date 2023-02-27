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