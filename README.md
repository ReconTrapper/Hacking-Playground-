# 🏗️ Multi-Target Cyber Security Sandbox & Automated Hacking Free Lab

A 100% free, legally sandboxed, and completely isolated multi-system penetration testing range engineered to deploy, provision, and attack enterprise-grade network environments inside a hypervisor abstraction layer.

---

## 🟢 New to Labs? Start Here! (Beginner's Quick Start)

Building a complete hacking range can feel overwhelming, but you can get this entire lab up and running by following these **3 Simple Milestones**:

* 🛠️ **Milestone 1: Prepare Your Laptop**
  - Download [VirtualBox](https://virtualbox.org) and a free [Windows Server 2025 Evaluation ISO](https://microsoft.com). 
  - Turn off **Memory Integrity** in your Windows Security settings so your laptop can give VirtualBox direct hardware access.
* 🌲 **Milestone 2: Spin Up Your Target Domain**
  - Create a new Windows Server VM, mount your ISO, and install the OS.
  - Open PowerShell inside your new Server and run our automated script: [\./04-Source-Code/Provision-Lab-Domain.ps1\]. Your domain controller is now active!
* 🩸 **Milestone 3: Populate and Attack**
  - Download the [BadBlood Framework](https://github.com) inside your Server VM and run \.\Invoke-BadBlood.ps1\ to fill your domain with thousands of test users automatically.
  - Link your **Kali Linux VM** to the same private network switch and start hacking!

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