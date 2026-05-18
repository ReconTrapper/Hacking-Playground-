#!/usr/bin/env python3
"""
================================================================================
HIGH-SPEED MULTI-THREADED NETWORK DISCOVERY ICMP PING SWEEPER
================================================================================
File:        ping_sweeper.py
Description: Sweeps private subnets for live targets using native multi-threading
             and cross-platform OS ICMP execution mappings.
================================================================================
"""

import os
import sys
import platform
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_host(ip_address: str) -> str:
    """
    Fires a single targeted ICMP echo request packet to a specified target host address.
    Returns the target IP address string if the host responds successfully.
    """
    # Detect the operating system configuration to apply proper ICMP counting flags
    current_os = platform.system().lower()
    
    if current_os == "windows":
        # -n = packet count, -w = timeout limit in milliseconds
        command = ["ping", "-n", "1", "-w", "500", ip_address]
    else:
        # -c = packet count, -W = timeout limit in seconds
        command = ["ping", "-c", "1", "-W", "1", ip_address]
        
    try:
        # Run process silently; suppress output streams from flooding terminal views
        with open(os.devnull, 'w') as devnull:
            result = subprocess.run(
                command, 
                stdout=devnull, 
                stderr=devnull, 
                check=True
            )
        if result.returncode == 0:
            return ip_address
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return ""

def execute_network_sweep(subnet_prefix: str, thread_count: int = 50) -> None:
    """Manages thread pools to execute parallel sweeps across the 254 host index range."""
    print("=" * 80)
    print(f" 📡 DISCOVERY ACTIVE: SWEEPING SUBNET RANGE -> {subnet_prefix}.0/24")
    print(f" [*] Allocation Engine Thread Pool workers: {thread_count}")
    print(f" [*] Scan Initialization Timestamp        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    live_hosts = []
    
    # Generate list of all possible hosts from .1 to .254
    target_ips = [f"{subnet_prefix}.{host_id}" for host_id in range(1, 255)]
    
    # Launch worker threads concurrently
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Map out tasks
        future_to_ip = {executor.submit(ping_host, ip): ip for ip in target_ips}
        
        for future in as_completed(future_to_ip):
            result_ip = future.result()
            if result_ip:
                print(f"    [+] [LIVE HOST DETECTED] -> {result_ip}")
                live_hosts.append(result_ip)
                
    print("\n" + "=" * 80)
    print(f" 🎉 SWEEP COMPLETE: Total discovered live targets: {len(live_hosts)}")
    print("=" * 80)
    for host in sorted(live_hosts, key=lambda x: int(x.split('.')[-1])):
        print(f"  👉 {host}")

if __name__ == "__main__":
    # Default to the LabNet virtual router subnet allocation blueprint
    target_subnet = "10.0.2"
    
    # Allow target override via terminal CLI arguments if passed
    if len(sys.argv) > 1:
        # If user passes 10.0.2.0, extract the base subnet segment
        parts = sys.argv[1].split('.')
        if len(parts) >= 3:
            target_subnet = f"{parts[0]}.{parts[1]}.{parts[2]}"
            
    try:
        execute_network_sweep(target_subnet, thread_count=64)
    except KeyboardInterrupt:
        print("\n[-] Scan execution aborted via user break signal. Exiting.")
        sys.exit(1)
