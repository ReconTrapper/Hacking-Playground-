# --- THE TRAPPER RANGE: ENTERPRISE ACTIVE DIRECTORY AUTOMATION ---
# Pre-checks for PowerShell Gallery dependencies
[void](Install-PackageProvider -Name nuget -Force -ForceBootstrap)
Install-Module -Name ActiveDirectoryDsc, AuditPolicyDsc -Force -AllowClobber -SkipPublisherCheck -ErrorAction SilentlyContinue

Import-Module ServerManager
Write-Host "[*] Extracting AD-DS binaries..." -ForegroundColor Cyan
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
$Password = ConvertTo-SecureString "Password123!" -AsPlainText -Force
Install-ADDSForest -DomainName "trapped.local" -SafeModeAdministratorPassword $Password -Force:$true -NoRebootOnCompletion:$false