import sys
import time
import os

def typing_effect(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class HackingPlaygroundGame:
    def __init__(self):
        self.player_handle = ""
        self.current_directory = "C:\\Users\\Operator>"
        self.discovered_hosts = []
        self.compromised_hosts = set()
        self.loot_inventory = []
        self.running = True

    def display_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("                 TRAVERSING THE COMMANDLINE")
        print("   An Interactive Penetration Testing Laboratory Simulator")
        print("       Integrated with: recontrapper Hacking Playground")
        print("=" * 70)
        self.player_handle = input("Enter your Hacker Handle: ").strip() or "Anon"
        typing_effect(f"\n[*] Initializing virtual environment for target infrastructure...")
        typing_effect("[*] Verification successful. Connected to local Ethical VM Lab network.\n")

    def run_command(self, cmd_input):
        parts = cmd_input.strip().split()
        if not parts:
            return
        base_cmd = parts[0].lower()
        if base_cmd == "help":
            self.show_help()
        elif base_cmd in ["dir", "ls"]:
            self.cmd_dir()
        elif base_cmd == "nmap":
            self.cmd_nmap(parts[1:])
        elif base_cmd == "msfconsole":
            self.cmd_msfconsole()
        elif base_cmd == "loot":
            self.cmd_loot()
        elif base_cmd in ["exit", "quit"]:
            typing_effect("[!] Closing console connection to ethical lab... Goodbye.")
            self.running = False
        else:
            print(f"'{base_cmd}' is not recognized as an internal or external command,")
            print("operable program or batch file. Type 'help' for available tools.")

    def show_help(self):
        print("\n=== AVAILABLE LAB PLATFORM COMMANDS ===")
        print("  dir / ls          - List contents of local workspace directory")
        print("  nmap [IP]         - Scan a target VM network host for open ports")
        print("  msfconsole        - Launch exploitation framework console")
        print("  loot              - View gathered flags, hashes, and credentials")
        print("  exit / quit       - Terminate session")

    def cmd_dir(self):
        print(f"\n Directory of {self.current_directory[:-1]}")
        print("2026-06-02  12:00 PM    <DIR>          .")
        print("2026-06-02  12:00 PM    <DIR>          ..")
        print("2026-06-02  01:15 PM               142 lab_targets.txt")
        print("2026-06-02  03:30 PM             2,048 custom_wordlist.txt")
        if "root_flag.txt" in self.loot_inventory:
            print("2026-06-02  03:54 PM                32 root_flag.txt")

    def cmd_nmap(self, args):
        if not args:
            print("[-] Usage: nmap [target_ip_address]")
            return
        target = args[0]
        typing_effect(f"\n[!] Initiating Nmap 7.92 stealth scan against {target}...")
        time.sleep(1.5)
        if target == "192.168.56.101":
            print(f"\nNmap scan report for {target}")
            print("Host is up (0.00045s latency).")
            print("PORT     STATE SERVICE     VERSION")
            print("21/tcp   open  ftp         vsftpd 2.3.4")
            print("80/tcp   open  http        Apache httpd 2.4.41")
            print("445/tcp  open  microsoft-ds Windows Server 2019 SMB")
            if target not in self.discovered_hosts:
                self.discovered_hosts.append(target)
        else:
            print(f"\n[!] Nmap: Note: Host {target} seems down. Skipping port scan.")

    def cmd_msfconsole(self):
        typing_effect("\n[********] Launching Metasploit Framework Console v6.3...", 0.01)
        print("       ,= ,-_-. =.")
        print("      ((_/)o o(\\_))")
        print("       `-'(. .)`-'")
        print("           \_/")
        while True:
            msf_input = input("msf6 > ").strip()
            if not msf_input:
                continue
            msf_parts = msf_input.split()
            msf_cmd = msf_parts[0].lower()
            if msf_cmd == "exit":
                typing_effect("[*] Exiting Metasploit framework...")
                break
            elif msf_cmd == "show" and len(msf_parts) > 1 and msf_parts[1] == "exploits":
                print("\nSimulated Exploits Available:")
                print("  1. exploit/unix/ftp/vsftpd_234_backdoor")
            elif msf_cmd == "use" and len(msf_parts) > 1:
                self.run_msf_exploit(msf_parts[1])
            else:
                print("Unknown exploit command. Type 'show exploits' or 'exit'.")

    def run_msf_exploit(self, exploit_path):
        if "vsftpd" in exploit_path:
            typing_effect(f"\n[*] Using configured exploit module: {exploit_path}")
            target_ip = input("msf6 exploit(...) > set RHOSTS: ")
            if target_ip == "192.168.56.101":
                typing_effect("[*] Triggering backdoor payload delivery mechanism...")
                time.sleep(2)
                typing_effect("[+] Command shell session 1 opened! Access granted.")
                typing_effect("[+] Current User: root", 0.01)
                if "root_flag.txt" not in self.loot_inventory:
                    self.loot_inventory.append("root_flag.txt")
                    print("\n[SUCCESS] Flag captured: flag{recontrapper_c_drive_breach}")
                self.compromised_hosts.add(target_ip)
            else:
                print("[-] Exploit failed: Host unreachable.")
        else:
            print("[-] Exploit path not recognized.")

    def cmd_loot(self):
        print("\n=== SYSTEM LOOT STORAGE ===")
        if not self.loot_inventory:
            print("[*] No loot collected yet.")
        else:
            for index, item in enumerate(self.loot_inventory, 1):
                print(f" [{index}] Collected: {item}")

    def start_loop(self):
        self.display_banner()
        while self.running:
            try:
                cmd_input = input(f"\n{self.current_directory} ")
                if cmd_input.strip() == "":
                    continue
                self.run_command(cmd_input)
            except KeyboardInterrupt:
                print("\n[!] Emergency abort signal received.")
                self.running = False

if __name__ == "__main__":
    game = HackingPlaygroundGame()
    game.start_loop()
