import socket

def scan_ports(target_host, start_port, end_port):
    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    target = input("Enter target host (e.g., 127.0.0.1): ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(target, start, end)
