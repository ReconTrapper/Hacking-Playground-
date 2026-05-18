#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

def grab_banner(target_socket: socket.socket) -> str:
    try:
        target_socket.send(b"\r\n")
        banner = target_socket.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner.replace('\n', ' ').replace('\r', '')
    except Exception:
        return "Service active (No banner returned)"

def scan_port(target_ip: str, port: int) -> dict:
    result = {"port": port, "status": "closed", "banner": ""}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

def run_port_scan(target_host: str, thread_count: int = 40) -> None:
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[❌] Fatal Error: Unable to resolve host target identity: {target_host}")
        return

    print("=" * 80)
    print(f" 📡 AUDITING ACTIVE TARGET PATH: {target_ip} ({target_host})")
    print(f" [*] Connection Threads Assigned: {thread_count}")
    print("=" * 80)

    open_ports_found = 0
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in COMMON_PORTS}
        for future in as_completed(future_to_port):
            audit_data = future.result()
            if audit_data["status"] == "open":
                open_ports_found += 1
                print(f"    [+] [PORT {audit_data['port']}/TCP OPEN] -> Banner: {audit_data['banner']}")

    print("=" * 80)
    print(f" 🎉 AUDIT COMPLETE: Discovered {open_ports_found} exposed services.")
    print("=" * 80)

if __name__ == "__main__":
    # Check if the user supplied an argument, if not prompt them directly
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        print("[?] No command line target provided.")
        target = input(" >>> Enter target IP or Hostname to scan: ").strip()
        
    if not target:
        print("[-] Error: No target specified. Exiting.")
        sys.exit(1)
        
    try:
        run_port_scan(target)
    except KeyboardInterrupt:
        print("\n[-] Active service sweep cancelled. Exiting.")
        sys.exit(0)
