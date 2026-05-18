# Windows Server 2025 AD-DS Lab Range Blueprint

## ?? Target Range Specifications
- **Operating System:** Windows Server 2025 Standard Evaluation (Desktop Experience)
- **Target Realm FQDN:** \	rapped.local\
- **Provisioned Testing Users:** ~2,500 fuzzed profiles via BadBlood Injection Framework
- **Static Address Allocation:** \10.0.2.8\ (LabNet Segment Interface)

## ? Deployment & Script Automation
To automatically provision the Active Directory Domain Services binaries and promote the root forest topology cleanly without graphical lag, utilize the following automation script:

\\\powershell
# Run inside fresh elevated target Server PowerShell session
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "trapped.local" -CreateDnsDelegation:\False -DatabasePath "C:\Windows\NTDS" -LogPath "C:\Windows\NTDS" -SysvolPath "C:\Windows\SYSVOL" -Force
\\\

## ?? Clipboard Integration Setup
1. Mount the Guest Additions via **Devices** -> **Insert Guest Additions CD Image...**
2. Launch \VBoxWindowsAdditions-amd64.exe\ as an Administrator inside the guest.
3. Reboot the Server and toggle **Devices** -> **Shared Clipboard** -> **Bidirectional**.
