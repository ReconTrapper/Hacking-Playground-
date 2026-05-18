# 🛡️ HACKING PLAYGROUND

[![Lab Status](https://shields.io)]()
[![Code Quality](https://shields.io)]()

An advanced, fully isolated cyber security research range and automated script portfolio. This workspace maps the complete attack lifecycle across virtualized subnets, vulnerable target architectures, and custom Python tooling.

---

## 🧭 SYSTEM ARCHITECTURE

```text
               [ PRIVATE NAT NETWORK: LabNet (10.0.2.0/24) ]
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       │                            │                            │
 ┌─────┴──────┐               ┌─────┴──────┐               ┌─────┴──────┐
 │ KALI LINUX │               │ META-TARGET│               │ OWASP WEB  │
 │ (Attacker) │               │ (Service)  │               │ (App Layer)│
 │ 10.0.2.3   │               │ 10.0.2.5   │               │ 10.0.2.X   │
 └────────────┘               └────────────┘               └────────────┘
```

---

## 📁 LABORATORY DIRECTORY LAYOUT

### 📦 01-Hypervisors
* Core virtualization virtualization software layouts, engines, and extensions tracking.

### 💿 02-ISO-Archive
* **`Linux/`** - Pristine distributions (Kali Linux installer bundles).
* **`Windows/`** - Clean evaluation operating system ISO disk blocks.

### 🖥️ 03-Active-VMs
* **`Kali-Control/`** - Your main weaponized offensive operating system.
* **`Meta-Target/`** - Metasploitable 2 vulnerability service sandbox.
* **`Web-Target/`** - OWASP Broken Web Applications project tier.
* **`Active-Directory/`** - Enterprise domain topologies containing **GOAD** and **BadBlood**.

### 🐍 04-Source-Code
* Master framework housing custom security scripts and synchronization tools.

---

## 🛠️ CUSTOM OFFENSIVE SCRIPT SUITE

### 📡 Network Reconnaissance (`Recon-Scanners/`)
* **`ping_sweeper.py`** - Multi-threaded ICMP node discovery mapping tool.
* **`advanced_scanner.py`** - Socket banner extractor with automated markdown report hooks.

### 🕸️ Web Exploitation Engineering (`Web-Exploitation/`)
* **`directory_bruter.py`** - Concurrent endpoint brute-forcer with custom user-agents.
* **`sqli_tester.py`** - Telemetry payload fuzzer targeting database logic flaws.
* **`xss_hunter.py`** - Reflected string sanity scanner for input fields.

### 📊 Audit Utilities (`Audit-Utilities/`)
* **`report_generator.py`** - Markdown compiler structuring raw logs into risk assessments.

### 🧹 Post-Exploitation Lifecycle (`Post-Exploitation/`)
* **`log_cleaner.py`** - Anti-forensic utility to truncate target `wtmp` and `btmp` log files.

---

## ⚙️ TARGET TROUBLESHOOTING DEPLOYMENT

### 🐧 Kioptrix Level 1
1. **SATA Kernel Panic Fix**: Remove virtual disk from SATA. Re-attach it under **`Controller: IDE`**.
2. **Network Driver Migration**: Choose **`Remove Configuration`** on initial boot to bind to `LabNet`.

### 🩸 Active Directory (BadBlood)
1. Run natively on a clean Windows Server Domain Controller as an Administrator.
2. Execute **`.\Invoke-BadBlood.ps1`** to inject 2,500+ randomized vulnerable objects into the domain schema.

---
*This playground is strictly locked inside a private virtual network loop. Do not bridge adapter interfaces to public networks.*

---

## CHAPTER 8: MASTER ECOSYSTEM ORDER OF OPERATIONS
To build a stable, fully integrated testing environment without performance degradation, execute the architectural deployment steps in this precise sequence:

### 📍 Phase 1: Host System Optimization (Windows 11 Host)
1. **Elevate Permissions**: Open an Administrator PowerShell window.
2. **Release CPU Virtualization Controls**: Execute `bcdedit /set hypervisorlaunchtype off`.
3. **Reboot the Host**: Restarts the hardware array, granting VirtualBox exclusive, unthrottled access to the Core i9 processing acceleration engines.

### 📍 Phase 2: Core Attack Infrastructure Deployment
1. **Launch Kali Linux**: Power on your main offensive VM shell inside VirtualBox.
2. **Restore Outbound Routing**: Run `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf` to guarantee external internet package downloads.
3. **Synchronize Scanners**: Navigate into `~/Hacking-Playground-/04-Source-Code/Recon-Scanners/` and execute your discovery tool suite.

### 📍 Phase 3: Vulnerable Target Deployment Matrix
1. **Legacy Linux System (Kioptrix Level 1)**: 
   * Extract hard disk containers natively. 
   * **Crucial Fix**: Attach the `.vmdk` disk to **`Controller: IDE`** (Delete SATA) to prevent Kernel Panics.
   * **Network Reset**: Select **`Remove Configuration`** on initial boot via the blue assistant prompt.
2. **Web Application Target (DC-1)**:
   * Select *File > Import Appliance* inside VirtualBox to load the `.ova` bundle cleanly.
3. **Enterprise Active Directory Domain (Windows Server Target)**:
   * Download the official 180-day Evaluation ISO directly into your `02-ISO-Archive/Windows/` repository path.
   * Create a new VirtualBox shell container, check **`Skip Unattended Installation`**, and allocate **`4096 MB RAM / 2 CPU Cores`**.
   * **Crucial Step**: Ensure you select the **`(Desktop Experience)`** image variant during the setup wizard sequence to guarantee a fully interactive graphical user interface.

### 📍 Phase 4: Network Isolation & Mapping
1. Open the Settings panel for **every target machine** inside VirtualBox.
2. Under **Network > Adapter 1**, toggle *Attached to:* straight to **`NAT Network`** and bind the name to your private **`LabNet`** interface router.
3. Boot all nodes concurrently and fire `python3 ping_sweeper.py` inside Kali to capture your active live target inventory addresses.
