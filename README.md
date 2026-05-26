# 🏗️ The Killbox: Trapper Range — Automated Setup

Copy and paste this entire block of code straight into a Windows **Administrator PowerShell** terminal window. This single pipeline will automatically install the hypervisor tools, manufacture your complete local file structure, download your required configuration scripts, and start the lab completely on autopilot.

```powershell
winget install Oracle.VirtualBox HashiCorp.Vagrant --accept-source-agreements --accept-package-agreements; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
mkdir "C:\Hacking-Playground\01-Hypervisors", "C:\Hacking-Playground\02-ISO-Archive\Windows", "C:\Hacking-Playground\03-Active-VMs\Windows-Lab", "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts", "C:\Hacking-Playground\04-Source-Code\Recon-Scanners", "C:\Hacking-Playground\.github\ISSUE_TEMPLATE" -Force | Out-Null; cd "C:\Hacking-Playground"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "Vagrantfile"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "04-Source-Code/Provision-Lab-Domain.ps1"
Invoke-WebRequest -Uri "https://githubusercontent.com" -OutFile "04-Source-Code/Add-Loot.ps1"
vagrant up
```

## 📊 What This Does on Your PC Instantly

1. **Installs the Prerequisites (Line 1):** Silently downloads and installs VirtualBox and Vagrant directly from official servers, and instantly refreshes your terminal's memory path so you don't have to restart your computer.
2. **Builds the Folders (Line 2):** Programmatically constructs your entire, structured subdirectory tree layout on your `C:\` drive.
3. **Downloads the Code (Lines 3-5):** Streams your clean infrastructure files and automated system setup tools straight from GitHub into their correct folder paths.
4. **Launches the Range (Line 6):** Boots your private virtual network adapters, downloads the stable target operating system images, and starts the lab completely hands-free.