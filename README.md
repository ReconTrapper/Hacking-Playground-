# 🏗️ Multi-Target Cyber Security Sandbox & Automated Hacking Free Lab

A 100% free, legally sandboxed, and completely isolated multi-system penetration testing range engineered to deploy, provision, and attack enterprise-grade network environments inside a hypervisor abstraction layer.

---

## 🟢 New to Labs? Start Here! (Beginner's Quick Start)

Building a complete hacking range can feel overwhelming, but you can get this entire lab up and running by choosing your preferred entry milestone:

### ⚡ Option A: The Fast & Lightweight Start (Linux Targets)
If you want to start hacking immediately without heavy setup or processing delay:
* 🌐 **The Web Path (DC-1 Target)**: Boot up the small pre-built DC-1 appliance. Link it to your network at 10.0.2.5 and immediately start using your Kali Linux VM to scan and exploit its vulnerable **Drupal CMS core software**.
* 🐧 **The Legacy Path (Kioptrix Target)**: Fire up the tiny legacy Kioptrix boot-to-root VM. *(Tip: Remap its drive controller to IDE to bypass modern SATA kernel panics!)* Practice basic banner grabbing, service scanning, and old-school Samba service exploitation.

### 🌲 Option B: The Advanced Enterprise Start (Windows AD-DS)
If you want to build a high-density corporate enterprise emulation matrix:
* 🛠️ **Step 1**: Provision a fresh Windows Server 2025 VM with 1 CPU core and 128MB VRAM using a free Evaluation ISO.
* 🤖 **Step 2**: Open PowerShell inside the server and run our automated generator script: [\./04-Source-Code/Provision-Lab-Domain.ps1\] to instantly stand up the 	rapped.local root forest.
* 🩸 **Step 3**: Download the [BadBlood Framework](https://github.com) inside the Server VM and execute \.\Invoke-BadBlood.ps1\ to automatically flood the directory database with thousands of test accounts, nested security groups, and hidden attack paths.

---

## 🛡️ Core Architecture: Isolation, Safety, & Licensing

* 🆓 **Zero-Cost Enterprise Engineering**: Built entirely utilizing official 180-day Microsoft Evaluation ISOs, open-source Linux appliances, and free community testing frameworks. No commercial licensing required.
* ☣️ **Strict Air-Gapped Sandbox Safety**: Hard-locked inside a private virtual network segment (**LabNet / 10.0.2.0/24**). It has no exposure or bridge to your physical Home LAN, providing a 100% safe environment to detonate malware, execute noisy fuzzing scripts, and run aggressive exploits.
* 💻 **Host Hardware Coexistence**: Specially aligned to utilize the Windows Hypervisor Platform (WHv) and Hyper-V paravirtualization provider interface. This allows high-speed virtualization testing while keeping **Windows 11 Core Isolation / Memory Integrity** fully active.

---

## 🎯 Active Lab Target Capabilities & Hacking Matrices

### 1. 🌲 Active Directory Enterprise Range (\	rapped.local\ | \10.0.2.8\)
* **Infrastructure:** Windows Server 2025 Standard Evaluation Active Directory Domain Services (AD-DS) Forest.
* **Target Density:** ~2,500 fuzzed users, organizational units (OUs), computers, and nested security groups via the BadBlood framework.
* **Exploitation Matrix:** Used to train in Active Directory post-exploitation attacks:
  * **Credential Hunting**: Password spraying, brute-forcing, and brute-forcing dictionaries.
  * **Kerberos Attacks**: AS-REP Roasting, Kerberoasting, and Silver/Golden ticket creation.
  * **Privilege Escalation**: Mapping complex object access paths with **BloodHound-python** and exploiting vulnerable Access Control Entries (ACEs).

### 2. 🌐 DC-1 Web Application Target (\10.0.2.5\)
* **Infrastructure:** Linux-based imported target web server.
* **Exploitation Matrix:** Dedicated to practicing Web App penetration testing, CMS enumeration, exploiting vulnerable **Drupal core software**, executing remote code execution (RCE), and hunting for local root privilege escalation paths.

### 🐧 3. Kioptrix Level 1 Legacy Target
* **Infrastructure:** Legacy Linux Boot-to-Root operating system (Remapped to an IDE storage controller to bypass SATA kernel panics).
* **Exploitation Matrix:** Focused on basic network service scanning, banner grabbing, and exploiting legacy service vulnerabilities (Samba, Apache, OpenSSL).

---

## 🗺️ Repository Structure
* 📂 **01-Hypervisors/**: VirtualBox hardware settings, optimization parameters, and Core Isolation safety mappings.
* 📂 **02-ISO-Archive/**: Local storage structures caching system installation media.
* 📂 **03-Active-VMs/**: Running lab ranges (\Kali-Control/\, \Meta-Target/\, \Web-Target/\, \Windows-Lab/\).
* 📂 **04-Source-Code/**: Production-ready automated tools:
  * [\Provision-Lab-Domain.ps1\]: Automated AD-DS forest generator script.
  * [\AD-DS-Lab-Setup.md\]: Deep technical build guide documentation.
  * \Recon-Scanners/\: Custom network automation tools, including \ping_sweeper.py\.

---
*Maintained globally by **ReconTrapper**. Engineered exclusively for legal, ethical, and advanced security research.*