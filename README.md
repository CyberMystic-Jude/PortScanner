# PortScanner

Description:

The Port Scanner tool is designed to help you scan open ports on a target host, which can be specified using either a URL (with or without 'https://') or an IP address. This tool is useful for checking the availability of network services on a remote host.

Usage:
- To scan ports on a target host specified by a URL: 
  `python portscan.py -u [URL]`

- To scan ports on a target host specified by an IP address:
  `python portscan.py -u [IP]`

Optional:
- You can specify a range of ports to scan by providing the starting and ending port numbers:
  `python portscan.py -u [URL or IP] -s [start_port] -e [end_port]`

If you don't specify the port range, the tool will scan ports from 1 to 65535 by default.

Installation:

-To install this tool in terminal

git clone https://github.com/CyberMystic-Jude/PortScanner

cd PortScanner/

chmod +x PortScanner.py 

python PortScanner.py -u [URL or IP] -s [start_port] -e [end_port]



Example:
- To scan all ports on example.com:
  `python portscan.py -u example.com`

- To scan ports in a specific range on an IP address:
  `python portscan.py -u 192.168.1.1 -s 80 -e 100`
