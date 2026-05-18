$TargetFolder = "C:\Hacking-Playground\04-Source-Code\Provisioning-Scripts"
if (-not (Test-Path $TargetFolder)) { New-Item -ItemType Directory -Path $TargetFolder | Out-Null }
Write-Host "[+] Provisioners builder asset stored." -ForegroundColor Green
