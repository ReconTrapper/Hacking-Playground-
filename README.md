# ??? The Killbox: Trapper Range � Automated Setup

The Trapper Range is a self-assembling, multi-target cybersecurity training arena. Instead of requiring manual operating system configuration or tedious user creation, this repository packages an entire enterprise laboratory environment down to a single automated deployment blueprint.

---

## ?? System Requirements Matrix

Before initializing the deployment, ensure your physical host computer meets these minimum specifications to prevent memory lockups:


| Resource | Minimum Requirement | Recommended Specification |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 / 11 (Home or Pro) | Windows 11 Pro |
| **Processor (CPU)** | 4 Cores (Intel i5 / AMD Ryzen 5) | 6+ Cores (Intel i7 / AMD Ryzen 7) |
| **Memory (RAM)** | **12 GB Physical RAM** | **16 GB to 32 GB Physical RAM** |
| **Storage Space** | **40 GB Free Space** | **60 GB Free Space (SSD)** |
| **Virtualization** | Intel VT-x or AMD-V (Enabled in BIOS) | Virtualization Enabled in BIOS |

> ?? **Prerequisite Note:** Open Windows Task Manager, navigate to the **Performance** tab, and confirm that **Virtualization: Enabled** is visible in the bottom right corner before proceeding.

---

## ?? The 1-Step Master Deployment Pipeline

Copy and paste this entire block of code straight into a Windows **Administrator PowerShell** terminal window. 

This single pipeline will instantly map your workspace folder layouts, download your required configuration scripts, verify your background hypervisor dependencies, and start the lab completely on autopilot.

```powershell
mkdir "C:\Hacking-Playground\01-Hypervisors", "C:\Hacking-Playground\02-ISO-Archive\Windows", "C:\Hacking-Playground\03-Active-VMs\Windows-Lab", "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts", "C:\Hacking-Playground\04-Source-Code\Recon-Scanners", "C:\Hacking-Playground\.github\ISSUE_TEMPLATE" -Force | Out-Null; cd "C:\Hacking-Playground"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "Vagrantfile"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "https://githubusercontent.com"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "https://githubusercontent.com"
winget install Oracle.VirtualBox HashiCorp.Vagrant --accept-source-agreements --accept-package-agreements; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
vVagrant up
```

## ?? What This Does on Your PC Instantly

1. **Builds the Workspace (Line 1):** Programmatically constructs your entire structured directory layout (01-Hypervisors, 02-ISO-Archive\Windows, 04-Source-Code, etc.) right on your root C:\ drive in under 1 second.
2. **Downloads the Code (Lines 2-4):** Streams your clean infrastructure configuration sheet and your automation tools directly into their designated folders from the secure GitHub source server.
3. **Installs Prerequisites (Line 5):** Silently pulls down VirtualBox and Vagrant directly from official servers, and instantly updates your terminal's memory map path so you don't have to restart your computer.
4. **Launches the Range (Line 6):** Boots your private virtual network adapters, downloads the stable target operating system images, and starts the lab completely hands-free.
