# 🏗️ The Killbox: Trapper Range

A 100% free, legally sandboxed, and completely isolated multi-system penetration testing range engineered to deploy, provision, and attack enterprise-grade network environments inside a hypervisor abstraction layer.

---

## 🟢 Deployment Methods & Target Modules

This laboratory ecosystem can be spun up, configured, and expanded using three distinct deployment layers depending on your learning goals and hardware specs.

### 🤖 Layer 1: The Automated One-Click Infrastructure Deployment (Vagrant Engine)
The fastest path to a complete lab! This automation uses infrastructure-as-code blueprints to silently install dependencies, configure the air-gapped private switches, and connect your virtual nodes with zero manual intervention.

1. Open your **Host Laptop PowerShell as an Administrator** and run this single line to silently install Vagrant with zero web forms or logins:
```powershell
winget install HashiCorp.Vagrant --silent --accept-source-agreements --accept-package-agreements
```
2. **Restart your PowerShell window** to refresh your system paths.
3. Navigate into your cloned repository root folder and type exactly **one command** to fire up your automated hacking range:
```bash
vagrant up
```

### 🌲 Module A: The Enterprise Active Directory Domain (Windows Server 2025 AD-DS)
Learn how corporate networks are engineered and broken. This component deploys a full enterprise forest running realistic misconfigurations and fuzzed target pathways.
* 🛠️ **Step 1**: Provision a fresh Windows Server 2025 VM using a free Evaluation ISO inside your `Windows-Lab` staging workspace.
  * 📥 **Download Link**: [Official Microsoft Evaluation Center](https://microsoft.com)
* 🤖 **Step 2**: Open PowerShell inside the server and run our automated generator script: `./04-Source-Code/Provision-Lab-Domain.ps1` to stand up the `trapped.local` root forest.
* 🩸 **Step 3**: Download BadBlood inside the VM and execute `.\Invoke-BadBlood.ps1` to fill the database with exactly **2,491 active fuzzed user profiles** and organizations built for password spraying and AS-REP roasting practice.
  * 📥 **Download Link**: [Official Davidprowe/BadBlood Repository](https://github.com)

### 🛰️ Module B: The Lightweight Boot-to-Root Catalog (Linux Target Labs)
Standalone Linux challenge targets linked seamlessly over your private sandbox switch to practice web exploitation, proxy hunting, and legacy service auditing.
* 🌐 **DC-1 Target (DC_1_Target)**: Boot up the Drupal web application instance. Map it to your subnet at `10.0.2.5` and use Kali to identify and exploit its CMS core vulnerabilities. 
  * 📥 **Download Link**: [Official VulnHub DC-1 Mirror](https://vulnhub.com)
* 🛡️ **SickOs 1.1 Target (SickOs_1_1)**: Practice shell hunting, proxy server misconfigurations, and reverse-routing vectors at `10.0.2.11`.
  * 📥 **Download Link**: [Official VulnHub SickOs 1.1 Mirror](https://vulnhub.com)
* 🐧 **Kioptrix Level 1 Target (Kioptrix_Level_1)**: Fire up the tiny legacy Linux box at `10.0.2.12` to target legacy Samba and Apache web stacks. *(Tip: Remap its drive controller to IDE to bypass modern SATA kernel panics!)*
  * 📥 **Download Link**: [Official VulnHub Kioptrix Entry](https://vulnhub.com)

---

## 🛡️ Core Architecture: Isolation, Safety, & Licensing
* 🆓 **Zero-Cost Enterprise Engineering**: Built entirely utilizing official 180-day Microsoft Evaluation ISOs, open-source Linux appliances, and free community testing frameworks. No commercial licensing required.
* ☣️ **Strict Air-Gapped Sandbox Safety**: Hard-locked inside a private virtual network segment (**LabNet / 10.0.2.0/24**). It has no exposure or bridge to your physical Home LAN, providing a 100% safe environment to detonate malware, execute noisy fuzzing scripts, and run aggressive exploits.
* 💻 **Host Hardware Coexistence**: Specially aligned to utilize the Windows Hypervisor Platform (WHv) and Hyper-V paravirtualization provider interface. This allows high-speed virtualization testing while keeping **Windows 11 Core Isolation / Memory Integrity** fully active.

---

## 📊 Weaponized Kali Linux Tool Matrix


| Phase Vector | Target Systems | Specialized Kali Hacking Tools | Primary Attack Capability |
| :--- | :--- | :--- | :--- |
| **Reconnaissance** | All Active Nodes | `nmap`, `fping` | Live host verification & port service sweeping |
| **Web App Audit** | `DC_1_Target`, `SickOs_1_1` | `gobuster`, `nikto`, `wpscan` | Hidden asset fuzzing & directory traversal leaks |
| **AD-DS Exploitation** | `trapped.local` (10.0.2.8) | `crackmapexec`, `netexec`, `impacket` | Multi-threaded password spraying & AS-REP ticket roasting |
| **Path Graphing** | `trapped.local` (10.0.2.8) | `bloodhound-python` | Graphing active access control control loops |
| **Behavioral Audit** | `Windows-Evaluator-Node` | Process Monitor, Wireshark | Monitoring dynamic script behavior safely |
| **Loot Architecture** | All Lab Credentials | `keepassxc-cli`, `Add-Loot.ps1` | Offline vault injection & credential tracking |

---

## 🎯 Active Lab Target Capabilities & Hacking Matrices
### 1. 🌲 Active Directory Enterprise Range (trapped.local | 10.0.2.8)
* **Infrastructure:** Windows Server 2025 Standard Evaluation Active Directory Domain Services (AD-DS) Forest.
* **Target Density:** ~2,491 fuzzed users, organizational units (OUs), computers, and nested security groups via the BadBlood framework.

### 2. 🌐 DC-1 Web Application Target (10.0.2.5)
* **Infrastructure:** Linux-based imported target web server running vulnerable **Drupal core software** for Remote Code Execution (RCE) training.

### 🐧 3. Kioptrix Level 1 Legacy Target (10.0.2.12)
* **Infrastructure:** Legacy Linux Boot-to-Root operating system optimized for old-school Samba/Apache service enumeration.

### 🛡️ 4. Windows Evaluation Node (10.0.2.15)
* **Infrastructure:** Windows 11 Enterprise Evaluation sandbox node built to monitor script executions and perform dynamic behavior analysis.
  
> [!CAUTION]
> **CRITICAL WINDOWS DL INSTRUCTION:** Do NOT attempt to use automated scripts (PowerShell, BITS, or curl) to download the Windows 11 Enterprise Evaluation ISO. Microsoft enforces strict anti-bot user-agent filtering that will silently fail and drop a corrupt 0 KB file. You **MUST** open the link manually in a real web browser and save the `.iso` file directly into the local repository asset folder path: `C:\Hacking-Playground\02-ISO-Archive\Windows\`.

---

## 🔑 Post-Exploitation: The Kali Loot Automation Framework
Once you successfully compromise a target node inside the range, you do not need to manually write passwords down. Your laboratory workspace incorporates a native, Kali-integrated automation tool to cleanly catalog your wins.

### 📟 How to Ingest Captured Credentials
Open your weaponized **Kali Linux Attacker VM** terminal, enter the repository tree, and execute our custom ingestion tool wrapper via the native Linux PowerShell Core engine:

```bash
# Launch the integrated menu system directly inside your Kali terminal
pwsh ./04-Source-Code/Add-Loot.ps1
```

### ⚙️ Under the Hood Mechanics
The script will present an interactive menu mapping out your targets. When you submit a credential pair, it instantly pipes the strings into the native Linux security layer (**`keepassxc-cli`**), saving your loot cleanly into your encrypted, air-gapped lab vault database.

---

## 🗺️ Repository Structure
* 📂 **01-Hypervisors/**: VirtualBox hardware settings, optimization parameters, and Core Isolation safety mappings.
* 📂 **02-ISO-Archive/**: Local storage structures caching system installation media.
* 📂 **03-Active-VMs/**: Running lab ranges (`Kali-Control/`, `Windows-Lab/`, `Windows-Evaluator-Node/`).
* 📂 **04-Source-Code/**: Production-ready automated tools:
  * [`Provision-Lab-Domain.ps1`]: Automated AD-DS forest generator script.
  * [`Add-Loot.ps1`]: Automated, multi-OS credential ingestion framework for KeePassXC.
  * [`AD-DS-Lab-Setup.md`]: Deep technical build guide documentation.

---
## 🤖 Engineering & Automation Attribution Disclaimer

* **AI-Assisted Architecture**: The scripts, deployment configurations, markdown blueprints, and interactive Wiki spaces hosted within this laboratory range were programmatically generated and optimized utilizing conversational AI frameworks.
* **Human-Driven Orchestration**: All virtualization topologies, manual debugging sequences, Git integration states, and hardware boundary alignments were engineered and verified directly by **ReconTrapper**. 
* **Intent**: Developed exclusively for accelerated educational tracking, ethical research, and high-performance offensive/defensive cybersecurity training paradigms.