import socket
def grab_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3.0)
            s.connect((ip, port))
            s.sendall(b"\r\n")
            print(f"[+] Banner: {s.recv(1024).decode('utf-8', errors='ignore').strip()}")
    except Exception as e: print(f"[-] Error: {e}")
if __name__ == "__main__":
    grab_banner(input("IP: "), int(input("Port: ")))