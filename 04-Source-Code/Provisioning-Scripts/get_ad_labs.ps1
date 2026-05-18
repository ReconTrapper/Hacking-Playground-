# Save the utility script to your provisioning scripts folder path
$ScriptPath = "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts\get_ad_labs.ps1"
Set-Content -Path $ScriptPath -Value (Get-Clipboard) -Force

# Run your one-click sync pipeline to back up your workspace changes online
PowerShell -ExecutionPolicy Bypass -File "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts\sync_to_github.ps1"

