import sys
import time
import os

def typing_effect(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class HackingPlaygroundGame:
    def __init__(self):
        self.player_handle = ""
        # Navigation State Trackers
        self.current_location = ["C:", "Level_1"] 
        self.discovered_hosts = []
        self.loot_inventory = []
        self.running = True
        
        # Room State Mechanics
        self.folder_1_solved = False
        self.folder_2_solved = False

    def get_prompt_path(self):
        return "\\".join(self.current_location) + ">"

    def display_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print("                 TRAVERSING THE COMMANDLINE")
        print("              [ LEVEL 1: THE DIRECTORY LABYRINTH ]")
        print("=" * 70)
        self.player_handle = input("Enter your Hacker Handle: ").strip() or "Trapper"
        typing_effect(f"\n[*] Deploying localized simulation cell for operator: {self.player_handle}...")
        typing_effect("[*] Environment verified. Type 'help' at any time to query toolbelt.\n")

    def run_command(self, cmd_input):
        parts = cmd_input.strip().split()
        if not parts:
            return
        
        base_cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if base_cmd == "help":
            self.show_help()
        elif base_cmd in ["dir", "ls"]:
            self.cmd_dir()
        elif base_cmd == "cd":
            self.cmd_cd(args)
        elif base_cmd == "tree":
            self.cmd_tree()
        elif base_cmd == "nmap":
            self.cmd_nmap(args)
        elif base_cmd == "loot":
            self.cmd_loot()
        elif base_cmd in ["exit", "quit"]:
            typing_effect("[!] Safe teardown execution initiated... Goodbye.")
            self.running = False
        else:
            print(f"'{base_cmd}' is not recognized as an internal or external command,")
            print("operable program or batch file. Type 'help' for available tools.")

    def show_help(self):
        print("\n=== SYSTEM ARCHITECTURE EMULATION HELP ===")
        print("  cd [dir]  - Change your current working workspace directory path")
        print("  dir / ls  - Enumerate details of objects inside the current space")
        print("  tree      - Graphically map structural directory sub-branches")
        print("  nmap [IP] - Scan target node (Requires structural intel data)")
        print("  loot      - Inspect local credentials stash and target indexes")
        print("  exit      - Terminate simulation cell connection")

    def cmd_dir(self):
        loc = self.current_location[-1]
        full_path_str = "\\".join(self.current_location)
        print(f"\n Directory of {full_path_str}")
        print("2026-06-02  04:15 PM    <DIR>          .")
        print("2026-06-02  04:15 PM    <DIR>          ..")

        if loc == "Level_1":
            print("2026-06-02  04:15 PM    <DIR>          folder_1")
            print("2026-06-02  04:15 PM    <DIR>          folder_2")
            print("2026-06-02  04:15 PM    <DIR>          folder_3")
        elif loc == "folder_1":
            print("2026-06-02  04:16 PM               420 cd_fundamentals.txt")
            if self.folder_1_solved:
                print("2026-06-02  04:16 PM                64 network_target_ip.txt")
        elif loc == "folder_2":
            print("2026-06-02  04:16 PM               840 ls_hidden_parameters.log")
            if self.folder_2_solved:
                print("2026-06-02  04:17 PM                32 target_subnet.txt")
        elif loc == "folder_3":
            print("2026-06-02  04:15 PM               105 dead_end_notice.txt")
            print("2026-06-02  04:15 PM               210 system_blueprint.dat")

    def cmd_cd(self, target):
        if not target:
            full_path_str = "\\".join(self.current_location)
            print(f"{full_path_str}")
            return

        # Handle moving backwards
        if target == "..":
            if len(self.current_location) > 2:
                self.current_location.pop()
            else:
                print("[-] Access Denied: Bound restriction error. Cannot traverse below Level_1 root.")
            return

        # Handle moving forward from Level_1 root
        if self.current_location[-1] == "Level_1":
            if target in ["folder_1", "folder_2", "folder_3"]:
                self.current_location.append(target)
                self.trigger_room_entry(target)
            else:
                print(f"[-] Error: System directory '{target}' does not exist.")
        else:
            print("[-] Structural Error: Subfolders are locked or empty. Use 'cd ..' to return.")

    def trigger_room_entry(self, folder_name):
        print(f"\n[+] Swapping active target path context to: {folder_name}")
        if folder_name == "folder_1":
            typing_effect("\n[ROOM 1: THE TRAVERSAL SHAFT]")
            typing_effect("This space demonstrates the mechanics of absolute vs relative directory jumps.")
            typing_effect("Hint: Type 'dir' to verify parameters, then input 'cd_fundamentals.txt' to look inside!")
        elif folder_name == "folder_2":
            typing_effect("\n[ROOM 2: THE ENUMERATION CELL]")
            typing_effect("This terminal matrix processes object listing functions ('ls' or 'dir').")
            typing_effect("Hint: Type 'ls_hidden_parameters.log' to extract the local workspace keys.")
        elif folder_name == "folder_3":
            typing_effect("\n[ROOM 3: THE MAP COMPARTMENT]")
            typing_effect("Your sensor array alerts you immediately: This room dead-ends into solid data blocks.")
            typing_effect("However, running a full visual breakdown command like 'tree' could expose structural links elsewhere...")

    def cmd_tree(self):
        print("\nC:\\Level_1")
        print("├── folder_1 (Navigation Puzzle Room)")
        print("│   └── [Hidden Link] -> Requires typing the full name of the .txt file")
        print("├── folder_2 (Enumeration Puzzle Room)")
        print("│   └── [Hidden File] -> Typing the log name reveals network landscape assets")
        print("└── folder_3 (Structural Map Compartment - DEAD END)")
        print("    └── [INTEL ALERT] -> Folder 1 can be passed by inspecting text objects.")
        print("    └── [INTEL ALERT] -> Folder 2 unlocks once its 'log' file parameters are entered.")

    def cmd_nmap(self, target):
        if not target:
            print("[-] Usage: nmap [target_ip_address]")
            return
        
        if not self.folder_1_solved or not self.folder_2_solved:
            print("[-] System Lockout: Missing required subnet and target IP maps from Folder 1 and 2.")
            return

        if target == "192.168.56.101":
            typing_effect(f"\n[!] Initializing full framework Nmap vector against: {target}...")
            time.sleep(1)
            print("PORT     STATE SERVICE     VERSION")
            print("22/tcp   open  ssh         OpenSSH 8.2p1")
            print("80/tcp   open  http        Apache httpd 2.4.41")
            print("\n[!] Level 1 Complete! Active exploit matrices staged for Level 2 deployment.")
            if "Target_VM_Map" not in self.loot_inventory:
                self.loot_inventory.append("Target_VM_Map")
        else:
            print(f"[-] Nmap: Error: Node reference '{target}' outside verified staging subnet boundary.")

    def cmd_loot(self):
        print("\n=== STAGED OPERATOR LOOT DEPLOYMENT ===")
        if not self.loot_inventory:
            print("[*] No operational network parameters captured yet.")
        else:
            for item in self.loot_inventory:
                print(f" [+] Verified Asset: {item}")

    def start_loop(self):
        self.display_banner()
        while self.running:
            try:
                cmd_input = input(f"\n{self.get_prompt_path()} ")
                normalized_input = cmd_input.strip().lower()
                current_room = self.current_location[-1]

                if normalized_input == "":
                    continue

                if current_room == "folder_1" and "cd_fundamentals.txt" in normalized_input:
                    typing_effect("\n[+] Success! You unlocked file variables. Target host isolated: 192.168.56.101")
                    self.folder_1_solved = True
                    if "Target_IP: 192.168.56.101" not in self.loot_inventory:
                        self.loot_inventory.append("Target_IP: 192.168.56.101")
                    continue
                
                if current_room == "folder_2" and "ls_hidden_parameters.log" in normalized_input:
                    typing_effect("\n[+] Success! Hidden directory flag parsed. Subnet isolated: 192.168.56.0/24")
                    self.folder_2_solved = True
                    if "Lab_Subnet: 192.168.56.0/24" not in self.loot_inventory:
                        self.loot_inventory.append("Lab_Subnet: 192.168.56.0/24")
                    continue
                    
                self.run_command(cmd_input)
            except KeyboardInterrupt:
                print("\n[!] Abort vector processed.")
                self.running = False

if __name__ == "__main__":
    game = HackingPlaygroundGame()
    game.start_loop()
