# ??? The Killbox: Trapper Range — Automated Setup

The Trapper Range is a self-assembling cybersecurity training arena. Instead of requiring manual operating system configuration or tedious user creation, this repository packages an entire enterprise laboratory environment down to a single automated deployment blueprint.

## ?? The 1-Step Master Deployment Pipeline

Copy and paste this entire block of code straight into a Windows **Administrator PowerShell** terminal window. 

This single pipeline will automatically check for and install the hypervisor engines, manufacture your complete multi-tiered local folder layout on your hard drive, download your required configuration scripts, and start the lab completely on autopilot.

```powershell
winget install Oracle.VirtualBox HashiCorp.Vagrant --accept-source-agreements --accept-package-agreements; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
mkdir "C:\Hacking-Playground\01-Hypervisors", "C:\Hacking-Playground\02-ISO-Archive\Windows", "C:\Hacking-Playground\03-Active-VMs\Windows-Lab", "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts", "C:\Hacking-Playground\04-Source-Code\Recon-Scanners", "C:\Hacking-Playground\.github\ISSUE_TEMPLATE" -Force | Out-Null; cd "C:\Hacking-Playground"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "Vagrantfile"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "https://githubusercontent.com"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "https://githubusercontent.com"
vagrant up
```

## ?? What This Does on Your PC Instantly

1. **Installs Prerequisites:** Silently pulls down VirtualBox and Vagrant directly from official servers, and instantly updates your terminal's memory map path so you don't have to restart your computer.
2. **Builds the Workspace:** Programmatically constructs your entire structured directory layout (`01-Hypervisors`, `02-ISO-Archive\Windows`, `04-Source-Code`, etc.) right on your root `C:\` drive.
3. **Downloads the Code:** Streams your clean infrastructure configuration sheet and your automation tools directly into their designated folders.
4. **Launches the Range (Vagrant up):** Boots your private virtual network adapters, downloads the stable target operating system images, and starts the lab completely hands-free.
