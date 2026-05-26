$DatabasePath = "C:\Hacking-Playground\02-ISO-Archive\Trapped-Lab-Loot.kdbx"
Clear-Host
Write-Host "--- LOOT INGESTION TOOL ---" -ForegroundColor Cyan
$TargetUser = Read-Host "Enter Username"
$MasterPass = Read-Host -AsSecureString "Enter KeePass Master Password"
Write-Host "[+] Logged entry for $TargetUser successfully." -ForegroundColor Green