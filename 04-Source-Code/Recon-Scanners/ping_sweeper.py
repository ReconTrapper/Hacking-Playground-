#!/usr/bin/env python3
"""
Module: High-Speed ICMP / Layer-3 Ping Sweeper
File: ping_sweeper.py
Description: Fast network mapping asset utilizing cross-platform subprocess wrappers.
"""
import os
import sys
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def ping_host(ip):
    # Determine local platform flag variables for active ping counts
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Execute native platform ping string engine and suppress console output noise
    command = f"ping {param} 1 -w 500 {ip} > NUL 2>&1" if platform.system().lower() == 'windows' else f"ping {param} 1 -W 1 {ip} > /dev/null 2>&1"
    
    response = os.system(command)
    if response == 0:
        print(f"  [+] Host Detected Active: {ip}")
        return ip
    return None

def main():
    print("=== LAYER-3 NETWORK MAPPING ENGINE: PING SWEEPER ===")
    subnet_cidr = input("Enter Network Range Descriptor (e.g., 10.0.2.0/24): ").strip()
    try:
        network = ipaddress.ip_network(subnet_cidr, strict=False)
    except ValueError as e:
        print(f"[!] Target Range Parse Failure: {e}")
        return

    print(f"[*] Dispatching asynchronous ping sweeps against {len(list(network.hosts()))} potential hosts...")
    active_hosts = []
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(ping_host, [str(ip) for ip in network.hosts()])
        for res in results:
            if res:
                active_hosts.append(res)
                
    print(f"\n[*] Mapping Finished. Identified {len(active_hosts)} active nodes on subnet.")

if __name__ == "__main__":
    main()
