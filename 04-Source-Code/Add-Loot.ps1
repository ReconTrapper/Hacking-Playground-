<#
.SYNOPSIS
    Dynamic Multi-OS Loot Ingestion Automation for KeePassXC on Kali Linux.
.DESCRIPTION
    Interactive framework designed to capture compromised credentials 
    and parse them directly into an encrypted KeePassXC offline database.
#>

$DatabasePath = "$HOME/Labs/trapped.local/loot/Trapped-Lab-Loot.kdbx"

Clear-Host
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " ?? RECONTRAPPER PLAYGROUND LOOT INGESTION TOOL ??" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Select the Target OS Range Compromised:" -ForegroundColor Yellow
Write-Host "1) Windows Server 2025 Active Directory Range"
Write-Host "2) DC-1 Drupal Web Application Node"
Write-Host "3) SickOs 1.1 Privilege Target Node"
Write-Host "4) Kioptrix Level 1 Legacy Linux Node"
Write-Host "==================================================" -ForegroundColor Cyan

$Selection = Read-Host "Choose Target Number (1-4)"

switch ($Selection) {
    "1" { $GroupTarget = "Active Directory Range"; $TargetIP = "10.0.2.8";  $Notes = "AD-DS Active User Account" }
    "2" { $GroupTarget = "Web Application Targets"; $TargetIP = "10.0.2.5";  $Notes = "DC-1 Drupal App Credential" }
    "3" { $GroupTarget = "Web Application Targets"; $TargetIP = "10.0.2.11"; $Notes = "SickOs Proxy/Shell Access Key" }
    "4" { $GroupTarget = "Domain Admins / Loot";    $TargetIP = "10.0.2.12"; $Notes = "Kioptrix Legacy Root Exploit" }
    Default { Write-Error "Invalid range selection."; Exit }
}

Write-Host ""
$TargetUser = Read-Host "Enter Compromised Username"
$TargetPass = Read-Host "Enter Cracked Password"
$MasterPass = Read-Host -AsSecureString "Enter KeePass Master Password"

$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($MasterPass)
$PlainMaster = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

$Env:KPXC_DIRTY = $PlainMaster
$Env:KPXC_DIRTY = $PlainMaster
$Env:KPXC_DIRTY = $PlainMaster
$CliCommand = "echo `$KPXC_DIRTY | keepassxc-cli add '$DatabasePath' '$GroupTarget/$TargetUser' --username '$TargetUser' --password-prompt --url '$TargetIP' --notes '$Notes'"
bash -c $CliCommand
Remove-Item Env:\KPXC_DIRTY
Remove-Item Env:\KPXC_DIRTY
Remove-Item Env:\KPXC_DIRTY

Write-Host ""
Write-Host "[+] SUCCESS: $TargetUser cleanly cataloged under '$GroupTarget' for Target IP $TargetIP!" -ForegroundColor Green
