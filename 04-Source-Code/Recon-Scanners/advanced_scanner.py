#!/usr/bin/env python3
"""
================================================================================
ADVANCED MULTI-THREADED TCP PORT SCANNER & BANNER GRABBER
================================================================================
File:        advanced_scanner.py
Description: Audits targeted hosts for open TCP pathways and extracts service
             banners to identify background system application architectures.
================================================================================
"""

import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Standard high-value target penetration testing ports to prioritize
COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    139,  # NetBIOS
    443,  # HTTPS
    445,  # SMB
    3306, # MySQL
    3389, # RDP
    8080  # HTTP-Alt
]

def grab_banner(target_socket: socket.socket) -> str:
    """Attempts to read raw service initialization banners from an open network port."""
    try:
        # Send an empty probe to force talkative services to respond if quiet
        target_socket.send(b"\r\n")
        banner = target_socket.recv(1024).decode('utf-8', errors='ignore').strip()
        # Clean up line breaks for clean terminal presentation
        return banner.replace('\n', ' ').replace('\r', '')
    except Exception:
        return "Service active (No banner returned)"

def scan_port(target_ip: str, port: int) -> dict:
    """Attempts to complete a standard 3-way TCP handshake over a specified socket."""
    result = {"port": port, "status": "closed", "banner": ""}
    
    # Establish network connection parameters using stream-oriented IPv4 TCP sockets
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set aggressive drop timeout so slow or blocked ports don't hang execution threads
    s.settimeout(1.5)
    
    try:
        connection = s.connect_ex((target_ip, port))
        if connection == 0:
            result["status"] = "open"
            result["banner"] = grab_banner(s)
    except Exception:
        pass
    finally:
        s.close()
        
    return result

def run_port_scan(target_host: str, thread_count: int = 30) -> None:
    """Spawns multi-threaded worker pools to sweep the targeted service range simultaneously."""
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[❌] Fatal Error: Unable to resolve host target identity: {target_host}")
        return

    print("=" * 80)
    print(f" 📡 AUDITING ACTIVE TARGET PATH: {target_ip} ({target_host})")
    print(f" [*] Connection Threads Assigned: {thread_count}")
    print(f" [*] Scan Initialization Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    open_ports_found = 0

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Submit execution tasks across our common tracking ports array
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in COMMON_PORTS}
        
        for future in as_completed(future_to_port):
            audit_data = future.result()
            if audit_data["status"] == "open":
                open_ports_found += 1
                print(f"    [+] [PORT {audit_data['port']}/TCP OPEN]")
                print(f"        └── Banner: {audit_data['banner']}\n")

    print("=" * 80)
    print(f" 🎉 AUDIT COMPLETE: Discovered {open_ports_found} exposed services.")
    print("=" * 80)

if __name__ == "__main__":
    # Fallback default target if no command line arguments are appended
    default_target = "10.0.2.1"
    
    if len(sys.argv) > 1:
        default_target = sys.argv[1]
        
    try:
        run_port_scan(default_target, thread_count=40)
    except KeyboardInterrupt:
        print("\n[-] Active service sweep cancelled by user interrupt signal. Exiting.")
        sys.exit(0)
