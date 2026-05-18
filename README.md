# 🏗️ Multi-Target Cyber Security Sandbox & Automated Hacking Free Lab

A 100% free, legally sandboxed, and completely isolated multi-system penetration testing range engineered to deploy, provision, and attack enterprise-grade network environments inside a hypervisor abstraction layer.

---

## 🟢 New to Labs? Start Here! (Beginner's Quick Start)

### 📥 Step 0: How to Pull This Code from GitHub
If you do not have this repository on your laptop yet, open **PowerShell** (on Windows) or a **Terminal** (on Linux/Mac) and run these commands to download the scripts and blueprints:

```bash
# 1. Clone the entire repository to your local machine cleanly
git clone https://github.com

# 2. Enter the project workspace folder
cd Hacking-Playground-

# 3. Access the automation folder
cd 04-Source-Code
```

---

### ⚡ Option A: The Fast & Lightweight Start (Linux & Boot-to-Root Catalog)
If you want to start hacking immediately without heavy setup, provision these localized pre-built appliances:
* 🌐 **DC-1 Target (DC_1_Target)**: Boot up the Drupal web application instance. Map it to your subnet at `10.0.2.5` and use Kali to identify and exploit its CMS core vulnerabilities.
* 🛡️ **SickOs 1.1 Target (SickOs_1_1)**: Deploy this classic intermediate boot-to-root machine to practice shell hunting, proxy server misconfigurations, and reverse-routing vectors.
* 🐧 **Kioptrix Level 1 Target (Kioptrix_Level_1)**: Fire up the tiny legacy Linux box. *(Tip: Remap its drive controller to IDE to bypass modern SATA kernel panics!)* Target its legacy Samba and Apache web stacks.

### 🌲 Option B: The Advanced Enterprise Start (Windows AD-DS Manual Setup)
If you want to build a high-density corporate enterprise emulation matrix manually:
* 🛠️ **Step 1**: Provision a fresh Windows Server 2025 VM with 1 CPU core and 128MB VRAM using a free Evaluation ISO inside your `Windows-Lab` staging workspace.
* 🤖 **Step 2**: Open PowerShell inside the server and run our automated generator script: `./04-Source-Code/Provision-Lab-Domain.ps1` to stand up the `trapped.local` root forest.
* 🩸 **Step 3**: Download BadBlood inside the VM and execute `.\Invoke-BadBlood.ps1` to fill the database with test accounts.

### 🤖 Option C: The One-Click Infrastructure-as-Code Setup (Vagrant App)
The ultimate beginner option! This allows your laptop to automatically pull the installation binaries, download the orchestrator engine without accounts, configure the private networks, and connect everything with zero manual steps.

1. Open your **Host Laptop PowerShell as an Administrator** and run this single line to silently install Vagrant with zero web forms or logins:
```powershell
winget install HashiCorp.Vagrant --silent --accept-source-agreements --accept-package-agreements
```
2. **Restart your PowerShell window** to refresh your system paths.
3. Navigate into your cloned repository root folder and type exactly **one command** to fire up your entire multi-VM automated hacking range:
```bash
vagrant up
```

---

## 🛡️ Core Architecture: Isolation, Safety, & Licensing
* 🆓 **Zero-Cost Enterprise Engineering**: Built entirely utilizing official 180-day Microsoft Evaluation ISOs, open-source Linux appliances, and free community testing frameworks. No commercial licensing required.
* ☣️ **Strict Air-Gapped Sandbox Safety**: Hard-locked inside a private virtual network segment (**LabNet / 10.0.2.0/24**). It has no exposure or bridge to your physical Home LAN, providing a 100% safe environment to detonate malware, execute noisy fuzzing scripts, and run aggressive exploits.
* 💻 **Host Hardware Coexistence**: Specially aligned to utilize the Windows Hypervisor Platform (WHv) and Hyper-V paravirtualization provider interface. This allows high-speed virtualization testing while keeping **Windows 11 Core Isolation / Memory Integrity** fully active.

---

## 🎯 Active Lab Target Capabilities & Hacking Matrices
### 1. 🌲 Active Directory Enterprise Range (trapped.local | 10.0.2.8)
* **Infrastructure:** Windows Server 2025 Standard Evaluation Active Directory Domain Services (AD-DS) Forest.
* **Target Density:** ~2,500 fuzzed users, organizational units (OUs), computers, and nested security groups via the BadBlood framework.
* **Exploitation Matrix:** Credential Hunting (Password spraying, brute-forcing), Kerberos Attacks (AS-REP/Kerberoasting), and Privilege Escalation mapping via **BloodHound-python**.

### 2. 🌐 DC-1 Web Application Target (10.0.2.5)
* **Infrastructure:** Linux-based imported target web server running vulnerable **Drupal core software** for Remote Code Execution (RCE) training.

### 🐧 3. Kioptrix Level 1 Legacy Target
* **Infrastructure:** Legacy Linux Boot-to-Root operating system optimized for old-school Samba/Apache service enumeration.

---

## 🗺️ Repository Structure
* 📂 **01-Hypervisors/**: VirtualBox hardware settings, optimization parameters, and Core Isolation safety mappings.
* 📂 **02-ISO-Archive/**: Local storage structures caching system installation media.
* 📂 **03-Active-VMs/**: Running lab ranges (`Kali-Control/`, `Meta-Target/`, `Web-Target/`, `Windows-Lab/`).
* 📂 **04-Source-Code/**: Production-ready automated tools.

---
*Maintained globally by **ReconTrapper**. Engineered exclusively for legal, ethical, and advanced security research.*