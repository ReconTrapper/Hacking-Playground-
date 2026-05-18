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
