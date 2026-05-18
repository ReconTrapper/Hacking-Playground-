# Windows Server 2025 AD-DS Lab Range Blueprint

## 💿 Target Range Specifications
- **Operating System:** Windows Server 2025 Standard Evaluation (Desktop Experience)
- **Target Domain Realm:** `trapped.local`
- **Active Range Target Interface:** `10.0.2.8` (LabNet Private Sandbox Switch)

---

## ⚡ Complete Lab Range Download Directory
To build or extend this multi-target ecosystem, utilize the verified official resource platforms below:

### 1. 🌲 Enterprise Active Directory Infrastructure
* **Windows Server 2025 Evaluation ISO**: Download via the [Official Microsoft Evaluation Center](https://microsoft.com).
* **Directory Fuzzing Engine Package**: Clone the live asset pool via the [Official Davidprowe/BadBlood Repository](https://github.com).

### ⚡ 2. Lightweight Linux & Boot-to-Root Catalog
* **DC-1 Web Target Appliance**: Ingest the vulnerable Drupal system via the [Official VulnHub DC-1 Mirror](https://vulnhub.com).
* **SickOs 1.1 Privilege Target**: Practice custom routing loops using the [Official VulnHub SickOs 1.1 Mirror](https://vulnhub.com).
* **Kioptrix Level 1 Legacy Target**: Audit ancient Samba configurations by deploying the [Official VulnHub Kioptrix Entry](https://vulnhub.com).

---

## 🤖 Automated AD-DS Local Execution Script
Run this script inside a fresh elevated target Server PowerShell session to handle the root forest configuration:
```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "trapped.local" -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -LogPath "C:\Windows\NTDS" -SysvolPath "C:\Windows\SYSVOL" -Force
```