<#
.SYNOPSIS
    Upgraded Hacking Lab Provisioner for Windows Host Environments.
#>
$ErrorActionPreference = "Stop"
$LabRoot = "C:\Hacking-Playground"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "🚀 INITIALIZING UPGRADED WINDOWS LAB PROVISIONING SUITE" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

$Directories = @(
    "$LabRoot\01-Hypervisors",
    "$LabRoot\02-ISO-Archive\Linux",
    "$LabRoot\02-ISO-Archive\Windows",
    "$LabRoot\03-Active-VMs\Kali-Control",
    "$LabRoot\03-Active-VMs\Meta-Target",
    "$LabRoot\03-Active-VMs\Web-Target",
    "$LabRoot\03-Active-VMs\Windows-Lab",
    "$LabRoot\04-Source-Code\Recon-Scanners",
    "$LabRoot\04-Source-Code\Web-Exploitation",
    "$LabRoot\04-Source-Code\Audit-Utilities",
    "$LabRoot\04-Source-Code\Provisioning-Scripts"
)

foreach ($Dir in $Directories) {
    if (-not (Test-Path $Dir)) {
        New-Item -ItemType Directory -Path $Dir | Out-Null
        Write-Host "   [+] Provisioned: $Dir" -ForegroundColor Green
    } else {
        Write-Host "   [-] Exists: $Dir" -ForegroundColor Yellow
    }
    New-Item -ItemType File -Path "$Dir\.gitkeep" -Force | Out-Null
}
Write-Host "`n[🎉] Complete! Workspace updated and initialized cleanly." -ForegroundColor Green
