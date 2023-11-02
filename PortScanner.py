import argparse
import socket
from urllib.parse import urlparse

print("                       ---Port Scanner---",end='\n')
print("*** For more details and Tools visit our GitHub page 'CyberMystic-Jude' ***")

def scan_ports(target_url, start_port, end_port):
    # Check if the URL starts with 'http://' or 'https://', and add 'http://' if not provided
    if not target_url.startswith('http://') and not target_url.startswith('https://'):
        target_url = 'http://' + target_url

    parsed_url = urlparse(target_url)
    target_host = parsed_url.netloc  # Extract the hostname from the URL

    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"Error: Unable to resolve the hostname '{target_host}' to an IP address.")
        return

    if not start_port:
        start_port = 1
    if not end_port:
        end_port = 65535

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")

            # Use a service identification tool to determine the purpose of the open port
            try:
                service_name = socket.getservbyport(port)
                print(f"Service name: {service_name}")
            except:
                print("Service name not found")

        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scanner -by Jude",epilog="Example:  python portscan.py -u [url] -s [starting port] -e [ending port] #Scans the open ports and services running on the target")
    parser.add_argument("-u", "--url", help="Target URL (e.g., www.youtube.com or https://www.youtube.com)")
    parser.add_argument("-s", "--start", type=int, help="Starting port")
    parser.add_argument("-e", "--end", type=int, help="Ending port")
    args = parser.parse_args()

    if not args.url:
        parser.print_help()
    else:
        scan_ports(args.url, args.start, args.end)

