# Active Directory Lab Range Setup & Fuzzing Deployment Blueprint

Comprehensive engineering guide for provisioning an isolated Windows Server 2025 target range optimized for fuzzing and Active Directory exploitation frameworks on a Windows 11 Home host machine.

---

## ??? Phase 1: Host System Configuration (Windows 11 Home)
Because Windows 11 Home lacks native Hyper-V management tools, VirtualBox requires exclusive hardware access to prevent installation freezes.

1. **Disable Memory Integrity / Code Isolation**
   - Navigate to \Windows Security\ -> \Device Security\ -> \Core Isolation Details\.
   - Toggle **Memory Integrity** to **OFF** to release exclusive low-level Intel VT-x hooks.
2. **Expose Guest Hypervisor API Support**
   - Run via elevated Host PowerShell to permit VirtualBox to interface safely with native Windows safety configurations if re-enabled post-install:
     \\\powershell
     Enable-WindowsOptionalFeature -Online -FeatureName "HypervisorPlatform" -All
     \\\
3. **Re-align VirtualBox Storage / Paravirtualization Engine**
   - Execute via host to tune performance loops:
     \\\powershell
     VBoxManage modifyvm "Windows-Server-Target" --paravirtprovider hyperv
     VBoxManage modifyvm "Windows-Server-Target" --nested-hw-virt on
     \\\

---

## ?? Phase 2: Windows Server 2025 Provisioning
1. **Hardware Allocation Parameters:**
   - **CPU Cores:** 1
   - **Video Memory (VRAM):** 128 MB
2. **OS Layout Configuration:**
   - **Selection:** \Windows Server 2025 Standard Evaluation (Desktop Experience)\
   - **Installation Method:** \Custom: Install Microsoft Server Operating System Only (advanced)\
   - **Storage Layout:** Wipe all pre-existing individual recovery and system partition footprints entirely on Disk 0. Highlight the unified \Disk 0 Unallocated Space\ block and click Next to allow the installer to automatically structure healthy GPT maps.

---

## ?? Phase 3: Active Directory Domain Services (AD-DS) Promotion
When clipboard integrations or internet paths are locked during bootstrap, deploy the environment promotion graphically via Server Manager inside the target VM:

1. Launch **Server Manager** inside the target VM.
2. Click **Manage** -> **Add Roles and Features** -> Select **Active Directory Domain Services** -> Click **Add Features** -> Proceed through installation.
3. Select the **Notification Warning Flag** in the upper right menu bar.
4. Click **Promote this server to a domain controller**.
5. Select **Add a new forest**. Set Root Domain Name to \	rapped.local\.
6. Set the Directory Services Restore Mode (DSRM) safe-mode password.
7. Bypass upstream DNS delegation warnings (expected behavior in private ranges) and accept system defaults.
8. Enforce the automated target system reboot. Your new authenticated realm is \TRAPPED\Administrator\.

---

## ?? Phase 4: Enabling Shared Utilities (VirtualBox Guest Additions)
Fixing clipboard mapping restrictions following forest generation:

1. Select **Devices** -> **Insert Guest Additions CD Image...** from the running VM window toolbar.
2. Open **File Explorer** inside the guest -> Go to **This PC** -> Double-click the mounted CD Drive.
3. Right-click **VBoxWindowsAdditions-amd64.exe** -> **Run as Administrator**.
4. Restart the guest environment.
5. In the VM window toolbar, set **Devices** -> **Shared Clipboard** -> **Bidirectional**.

---

## ?? Phase 5: Fuzzing via BadBlood
With the clipboard bridge verified, copy and run the automated execution block via an elevated Guest PowerShell window to dynamically populate thousands of randomized user profiles, ACLs, and organizational units:

\\\powershell
New-Item -ItemType Directory -Force -Path "C:\BadBlood"
Set-Location -Path "C:\BadBlood"
Invoke-WebRequest -Uri "https://github.com" -OutFile "C:\BadBlood\master.zip"
Expand-Archive -Path "C:\BadBlood\master.zip" -DestinationPath "C:\BadBlood" -Force
Set-ExecutionPolicy Bypass -Scope Process -Force
Set-Location -Path "C:\BadBlood\BadBlood-master"
.\Invoke-BadBlood.ps1
\\\
*When prompted by the console script, type \adblood\ exactly to kick off the randomization loop matrix.*
