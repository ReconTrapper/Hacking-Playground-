#!/usr/bin/env python3
"""
================================================================================
INTEGRATED AUTO-REPORTING MULTI-THREADED TCP PORT SCANNER
================================================================================
File:        advanced_scanner.py
Description: Audits targeted hosts for open TCP pathways, extracts service
             banners, and automatically invokes the audit reporting engine.
================================================================================
"""

import socket
import sys
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Injecting local path lookups so Python can natively find our report utility module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Audit-Utilities')))
try:
    from report_generator import AuditReporter
except ImportError:
    AuditReporter = None

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

def grab_banner(target_socket: socket.socket) -> str:
    try:
        target_socket.send(b"\r\n")
        banner = target_socket.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner.replace('\n', ' ').replace('\r', '')
    except Exception:
        return "Service active (No banner returned)"

def scan_port(target_ip: str, port: int) -> dict:
    result = {"port": port, "status": "closed", "banner": "", "service": "Unknown"}
    
    # Simple port-to-service mapping lookup dictionary
    service_map = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP", 443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP"}
    result["service"] = service_map.get(port, "Unknown")
    
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
        print(f"\n[❌] Fatal Error: Unable to resolve host target: {target_host}")
        return

    print("=" * 80)
    print(f" 📡 AUDITING ACTIVE TARGET PATH: {target_ip} ({target_host})")
    print("=" * 80)

    open_findings = []

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in COMMON_PORTS}
        for future in as_completed(future_to_port):
            audit_data = future.result()
            if audit_data["status"] == "open":
                print(f"    [+] [PORT {audit_data['port']}/TCP OPEN] -> Banner: {audit_data['banner']}")
                open_findings.append(audit_data)

    print("=" * 80)
    print(f" 🎉 SCAN COMPLETE: Discovered {len(open_findings)} exposed services.")
    print("=" * 80)

    # Trigger Automated Report Generation Engine if module link is active
    if AuditReporter and open_findings:
        print("\n[*] Initializing automated pipeline report generation...")
        reporter = AuditReporter(target_ip)
        for item in open_findings:
            # Determine basic risk matrix heuristics based on standard service exposure rules
            risk = "High" if item["port"] in [21, 23, 445] else "Medium" if item["port"] in [22, 3306, 3389] else "Low"
            fix = "Update service configurations or close unneeded open firewall entries."
            reporter.add_finding(item["service"], item["port"], item["banner"], risk, fix)
        
        saved_file = reporter.compile_report()
        print(f"[🎉] AUTO-REPORT ACQUIRED -> {saved_file}\n" + "=" * 80)
    elif not AuditReporter:
        print("[⚠️] System Notice: report_generator.py core reporting utility module was missing.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        print("[?] No command line target provided.")
        target = input(" >>> Enter target IP or Hostname to scan: ").strip()
        
    if not target:
        sys.exit(1)
    run_port_scan(target)
