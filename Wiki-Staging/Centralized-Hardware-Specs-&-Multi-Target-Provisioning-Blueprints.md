# Centralized Hardware Specs & Multi-Target Provisioning Blueprints

Because **The Killbox: Trapper Range** is engineered using flexible, Infrastructure-as-Code principles, its resource footprint can be dynamically scaled and adapted to match any testing machine hardware.

---

## 💻 Hardware Adaptation Matrix


| Target Profile | Minimum Host Specs | Guest Resource Split | Concurrent Target Capability |
| :--- | :--- | :--- | :--- |
| **1-on-1 Isolated Track** | **8GB RAM** / 4 CPU Cores | Kali (2GB) + Windows Server (3GB) | Run the Attacker Controller node + **only 1 target machine** concurrently. |
| **Full Corporate Pivot** | **16GB RAM** / 6+ CPU Cores | Kali (2GB) + Server (4GB) + Web (1GB) | Run the **entire multi-OS playground catalog** simultaneously. |

* **Storage Footprint**: Users require **30GB to 40GB of free Solid State Drive (SSD) storage** space to hold the hypervisor base installation files (`.vdi` and `.vmdk` files).
* **Paravirtualization Driver Core Line**: VirtualBox is configured to use Microsoft's native Hyper-V driver (`hyperv`). This allows full lab processing speeds while keeping **Windows 11 Core Isolation / Memory Integrity active** on your physical host laptop.

---

## 🛠️ The 3 Ways to Deploy the Range

Depending on your engineering experience and laptop resource limits, you can stand up the lab environment using three distinct methods:

### ⚡ Option A: The Fast & Lightweight Start (Linux Boot-to-Root Catalog)
* **Resource Profile**: Ultra-low footprint (Fits 8GB RAM laptops easily).
* **The Blueprint**: Users skip the massive Windows Server configuration and deploy pre-built, lightweight Linux appliances like **DC-1 (Vulnerable Drupal CMS Core)**, **SickOs**, or **Kioptrix Level 1**.
* **Loot Integration**: Compatible with our local automated password-vault ingestion script (`Add-Loot.ps1`) to pipe credentials straight to an offline KeePassXC database.

### 🌲 Option B: The Advanced Enterprise Start (Windows AD-DS Manual Setup)
* **Resource Profile**: Moderate footprint (Requires 8GB–16GB RAM laptops).
* **The Blueprint**: Users download an official 180-day Microsoft Evaluation Server ISO, run our automated `Provision-Lab-Domain.ps1` script to stand up the root forest forest (`trapped.local`), and execute BadBlood to inject **2,491 active fuzzed user profiles** into the NTDS database structure.

### 🤖 Option C: The One-Click DevSecOps Infrastructure Setup (Vagrant App)
* **Resource Profile**: High-performance optimization (Requires a 16GB RAM laptop for full simultaneous boot-up loops).
* **The Blueprint**: The absolute gold standard for automation. Users type exactly one terminal command (`vagrant up`). The software silently downloads the components, sets up the air-gapped sandbox network interfaces, and boots the entire multi-OS target catalog completely unattended.