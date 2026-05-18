#!/usr/bin/env python3
import sys, os, socket, ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_ping(ip):
    for port in [21, 22, 23, 80, 443]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            if s.connect_ex((ip, port)) == 0: return True
    return False

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            if s.connect_ex((ip, port)) == 0:
                print(f"  [+] Port {port:5} is OPEN")
    except: pass

def main():
    print("=== COGNITIVE RECONNAISSANCE ENGINE INITIALIZED ===")
    mode = input("Select [1] Subnet Discovery or [2] Port Scan: ").strip()
    if mode == "1":
        net = input("Enter CIDR Subnet (e.g., 10.0.2.0/24): ")
        print("[*] Shuffling workers to sweep block...")
        with ThreadPoolExecutor(max_workers=50) as ex:
            hosts = [str(ip) for ip in ipaddress.ip_network(net, strict=False).hosts()]
            results = ex.map(lambda h: (h, check_ping(h)), hosts)
            for h, status in results:
                if status: print(f"  [+] Host Detected Alive: {h}")
    elif mode == "2":
        ip = input("Enter Target IP: ")
        print(f"[*] Auditing target node {ip}...")
        with ThreadPoolExecutor(max_workers=100) as ex:
            [ex.submit(scan_port, ip, p) for p in range(1, 1025)]

if __name__ == "__main__": main()
