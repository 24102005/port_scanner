import socket
from datetime import datetime

# Ask user for input
target = input("Enter target host (IP or domain): ")
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1023): "))

target_ip = socket.gethostbyname(target)  # Translate hostname to IPv4

print("=" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Scanning Ports: {start_port} to {end_port}")
print("Scanning started at:", datetime.now())
print("=" * 50)

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nScan interrupted by user")
except socket.gaierror:
    print("\nHostname could not be resolved")
except socket.error:
    print("\nServer not responding")
