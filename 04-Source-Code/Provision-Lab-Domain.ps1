<#
.SYNOPSIS
    Automated Active Directory Domain Services Provisioning Script for Hacking Labs.
.DESCRIPTION
    Installs core AD-DS feature binaries and promotes the local host machine 
    to a Root Domain Controller under the 'trapped.local' schema layout.
#>

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "This orchestration payload requires elevated Administrator privileges. Restart terminal."
    Exit
}

Write-Host "[*] Initializing Active Directory Feature Binary Extraction..." -ForegroundColor Cyan
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

Write-Host "[+] Binary Pool Validated. Initializing Active Directory Forest Promotion..." -ForegroundColor Green
Write-Host "[!] Note: System will automatically reboot upon successful configuration." -ForegroundColor Yellow

Install-ADDSForest -DomainName "trapped.local" -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -LogPath "C:\Windows\NTDS" -SysvolPath "C:\Windows\SYSVOL" -Force
