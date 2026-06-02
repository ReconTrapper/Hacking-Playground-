# --- THE TRAPPER RANGE: POST-EXPLOITATION LOOT MATRIX ---
# Bypasses local MS Office dependencies by pulling ImportExcel from the Gallery over the wire
Install-Module -Name ImportExcel -Force -AllowClobber -SkipPublisherCheck -ErrorAction SilentlyContinue

$DatabasePath = "C:\Hacking-Playground\02-ISO-Archive\Trapped-Lab-Loot.kdbx"
Clear-Host
Write-Host "--- LOOT INGESTION TOOL ---" -ForegroundColor Cyan
$TargetUser = Read-Host "Enter Username"
$MasterPass = Read-Host -AsSecureString "Enter KeePass Master Password"

# Structural array blueprint to create styled spreadsheets natively
$LootData = [PSCustomObject]@{
    Timestamp = (Get-Date).ToString()
    TargetUser = $TargetUser
    Status     = "Captured Securely"
}
$LootData | Export-Excel -Path "C:\Hacking-Playground\02-ISO-Archive\Trapper-Loot-Ledger.xlsx" -AutoSize -TableStyle Medium2
Write-Host "[+] Logged entry for $TargetUser successfully into Excel sheet database." -ForegroundColor Green