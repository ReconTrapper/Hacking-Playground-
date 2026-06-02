import sys
import time
import os

def typing_effect(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

class HackingPlaygroundGame:
    def __init__(self):
        self.player_handle = ""
        self.current_location = ["C:", "Level_1"] 
        self.loot_inventory = []
        self.running = True
        self.folder_1_solved = False
        self.folder_2_solved = False
        self.advanced_rooms_unlocked = False

    def get_prompt_path(self):
        return "\\".join(self.current_location) + ">"

    def display_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 75)
        print("              🎯   TRAVERSING THE COMMANDLINE: LEVEL 1   🎯")
        print("              [ MISSION: INTEL ENUMERATION & CAPTURE ]")
        print("=" * 75)
        self.player_handle = input("⚡ Initialize Operator Handle: ").strip() or "Trapper"
        print("\n" + "•" * 75)
        typing_effect(f"📡 [ INBOUND WIRELESS FEED FROM RECON-LEAD ]")
        typing_effect(f"» \"Listen up, {self.player_handle}. We just breached their internal network hub.")
        typing_effect("» The target's infrastructure is hidden somewhere inside these subdirectories.")
        typing_effect("» Before we execute an exploit payload, we need basic network coordinates.")
        typing_effect("» Let's test your interface connection. Type 'help' to verify your tool arsenal!\"")
        print("•" * 75 + "\n")

    def run_command(self, cmd_input):
        parts = cmd_input.strip().split()
        if not parts:
            return
        base_cmd = parts[0].lower()
        args = " ".join(parts[1:]) if len(parts) > 1 else ""
        if base_cmd == "help":
            self.show_help()
        elif base_cmd in ["dir", "ls"]:
            self.cmd_dir()
            self.check_and_trigger_unlock()
        elif base_cmd == "cd":
            self.cmd_cd(args)
        elif base_cmd == "tree":
            self.cmd_tree()
            self.check_and_trigger_unlock()
        elif base_cmd in ["cat", "type"]:
            self.cmd_cat(args)
        elif base_cmd == "nmap":
            self.cmd_nmap(args)
        elif base_cmd == "loot":
            self.cmd_loot()
        elif base_cmd in ["exit", "quit"]:
            if self.current_location[-1] == "exit_gate":
                typing_effect("🏹 [!] Session decoupled cleanly. Goodbye!")
                self.running = False
            else:
                print("❌ [-] Secure Teardown Blocked: Use 'cd exit_gate' to leave safely.")
        else:
            print(f"❌ '{base_cmd}' is not recognized. Type 'help' for tactical gear layout.")

    def show_help(self):
        print("\n=== COMMAND ARSENAL ===")
        print("  cd [folder]  - Travel into directories")
        print("  dir / ls     - Scan and display objects residing in the immediate room")
        print("  tree         - Deploy a mapping radar sweep to view all sector paths")
        print("  cat [file]   - Force open and read a target data file")
        print("  loot         - Verify your tactical inventory hashes")
        if self.advanced_rooms_unlocked:
            print("\n🚨 === ADVANCED CHANNELS UNLOCKED ===")
            print("  cd nmap_room / cd loot_vault / cd exit_gate")

    def check_and_trigger_unlock(self):
        if not self.advanced_rooms_unlocked:
            self.advanced_rooms_unlocked = True
            print("\n" + "🔥" * 37)
            typing_effect("📡 [GRID CHANNELS]: Advanced tactical rooms have emerged from the noise:")
            print("  » cd nmap_room | cd loot_vault | cd exit_gate")
            print("🔥" * 37)

    def cmd_dir(self):
        loc = self.current_location[-1]
        full_path_str = "\\".join(self.current_location)
        print(f"\n📂 Sector Enumerate Map: {full_path_str}")
        if loc == "Level_1":
            print("<DIR>          folder_1\n<DIR>          folder_2\n<DIR>          folder_3")
            if self.advanced_rooms_unlocked:
                print("<DIR>          nmap_room\n<DIR>          loot_vault\n<DIR>          exit_gate")
        elif loc == "folder_1":
            print("420 bytes      cd_fundamentals.txt")
        elif loc == "folder_2":
            print("840 bytes      ls_hidden_parameters.log")
        elif loc == "folder_3":
            print("105 bytes      dead_end_notice.txt")
        elif loc == "nmap_room":
            print("512 bytes      nmap_binary.exe\n🎯 Use 'nmap 192.168.56.101' here once files are hacked.")

    def cmd_cd(self, target):
        if not target:
            return
        if target == "..":
            if len(self.current_location) > 2:
                self.current_location.pop()
            return
        if self.current_location[-1] == "Level_1":
            valid = ["folder_1", "folder_2", "folder_3"]
            if self.advanced_rooms_unlocked:
                valid.extend(["nmap_room", "loot_vault", "exit_gate"])
            if target in valid:
                self.current_location.append(target)
                self.trigger_room_entry(target)
                self.check_and_trigger_unlock()
            else:
                print(f"❌ Scouting Error: '{target}' not found.")
        else:
            print("❌ Location Locked. Use 'cd ..' to return to the hub matrix.")

    def trigger_room_entry(self, name):
        if name == "folder_1":
            typing_effect("\n🌲 [ROOM 1: THE TRAVERSAL SHAFT]\n» Run: 'cat cd_fundamentals.txt'")
        elif name == "folder_2":
            typing_effect("\n🌲 [ROOM 2: THE ENUMERATION CELL]\n» Run: 'cat ls_hidden_parameters.log'")
        elif name == "folder_3":
            typing_effect("\n🌲 [ROOM 3: THE MAP COMPARTMENT]\n» A dead end workspace. Try running 'tree'.")

    def cmd_cat(self, target):
        current_room = self.current_location[-1]
        if not target:
            return
        if current_room == "folder_1" and "cd_fundamentals.txt" in target.lower():
            typing_effect("\n📄 TARGET HOST IP ADDRESS LOCATED -> [ 192.168.56.101 ]")
            self.folder_1_solved = True
            if "Target_IP" not in self.loot_inventory: self.loot_inventory.append("Target_IP")
        elif current_room == "folder_2" and "ls_hidden_parameters.log" in target.lower():
            typing_effect("\n📄 TARGET SUBNET RANGE LOCATED -> [ 192.168.56.0/24 ]")
            self.folder_2_solved = True
            if "Lab_Subnet" not in self.loot_inventory: self.loot_inventory.append("Lab_Subnet")
        else:
            print("❌ File object not found inside this room.")

    def cmd_tree(self):
        print("\n🗺️ [RADAR RADIAL MAP]\nC:\\Level_1\n├── folder_1\n├── folder_2\n└── folder_3")

    def cmd_nmap(self, target):
        if self.current_location[-1] != "nmap_room":
            print("❌ Run nmap inside '\\nmap_room'.")
            return
        if not self.folder_1_solved or not self.folder_2_solved:
            print("❌ Intel data missing from Folders 1 & 2.")
            return
        if target == "192.168.56.101":
            typing_effect("\n⚡ FIRING PORT SCAN VECTOR...\nPORT     STATE SERVICE\n22/tcp   open  ssh\n80/tcp   open  http\n🏆 Level 1 cleared completely, Hunter!")
        else:
            print("❌ Target outside subnet range.")

    def cmd_loot(self):
        print(f"\n🏆 === TROPHY STASH ===\nCollected: {self.loot_inventory}")

    def start_loop(self):
        self.display_banner()
        while self.running:
            try:
                cmd_input = input(f"\n{self.get_prompt_path()} ")
                if cmd_input.strip() == "": continue
                self.run_command(cmd_input)
            except KeyboardInterrupt:
                self.running = False

if __name__ == "__main__":
    game = HackingPlaygroundGame()
    game.start_loop()
