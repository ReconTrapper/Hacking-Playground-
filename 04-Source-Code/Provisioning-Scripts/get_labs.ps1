# Write the downoader code to your tracked automated provisioning scripts folder
$ProvisioningPath = "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts\get_labs.ps1"
Set-Content -Path $ProvisioningPath -Value (Get-Clipboard) -Force

# Fire your automated sync engine to backup your workspace modifications to GitHub
PowerShell -ExecutionPolicy Bypass -File "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts\sync_to_github.ps1"

