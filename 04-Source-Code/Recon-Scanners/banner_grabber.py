#!/usr/bin/env python3
"""
Module: Automated Service Banner Grabber
File: banner_grabber.py
Description: Probes open ports to extract service version signatures.
"""
import socket
import sys

def grab_banner(ip, port):
    print(f"\n[*] Interrogating service signature on {ip}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3.0)
            s.connect((ip, port))
            
            # Send standard application trigger request strings
            if port == 80:
                s.sendall(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
            elif port == 21:
                # FTP servers naturally broadcast banners on connection
                pass
            else:
                s.sendall(b"\r\n")
                
            banner = s.recv(1024)
            if banner:
                clean_banner = banner.decode('utf-8', errors='ignore').replace('\r', '').replace('\n', ' ')
                print(f"  [+] Signature Recovered: {clean_banner.strip()[:80]}")
            else:
                print("  [-] Connection established, but no text banner string returned.")
    except socket.timeout:
        print("  [-] Request Timed Out. Service did not respond within window.")
    except Exception as e:
        print(f"  [-] Connection Exception: {e}")

def main():
    print("=== LAYER-7 ENUMERATION ENGINE: BANNER GRABBER ===")
    target_ip = input("Enter Target IP: ").strip()
    try:
        target_port = int(input("Enter Target Port (e.g., 21, 22, 80): ").strip())
    except ValueError:
        print("[!] Port constraint verification failed.")
        return
    grab_banner(target_ip, target_port)

if __name__ == "__main__":
    main()
