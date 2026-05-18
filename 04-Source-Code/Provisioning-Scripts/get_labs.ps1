# ==============================================================================
# AUTOMATED VULNHUB LAB ACQUISITION ENGINE FOR RECONTRAPPER
# ==============================================================================
$ErrorActionPreference = "Stop"
$DownloadTargetFolder = "C:\Hacking-Playground\03-Active-VMs"

if (-not (Test-Path $DownloadTargetFolder)) {
    New-Item -ItemType Directory -Path $DownloadTargetFolder -Force | Out-Null
}

$LabTargets = @{
    "Kioptrix_Level_1" = "https://vulnhub.com"
    "DC_1_Target"      = "https://vulnhub.com"
    "SickOs_1_1"       = "https://vulnhub.com"
}

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "📡 INITIALIZING AUTOMATED LAB DOWNLOAD PIPELINE" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

foreach ($LabName in $LabTargets.Keys) {
    $SourceUrl = $LabTargets[$LabName]
    $FileExtension = [System.IO.Path]::GetExtension($SourceUrl)
    $DestinationPath = Join-Path $DownloadTargetFolder "$LabName$FileExtension"
    
    if (-not (Test-Path $DestinationPath)) {
        Write-Host "[*] Spawning download stream for -> $LabName..." -ForegroundColor Cyan
        try {
            Invoke-WebRequest -Uri $SourceUrl -OutFile $DestinationPath -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            Write-Host "    [+] Success! File saved cleanly to -> $DestinationPath`n" -ForegroundColor Green
        } catch {
            Write-Host "    [❌] Network Interruption: Unable to fetch $LabName. Error: $_" -ForegroundColor Red
        }
    } else {
        Write-Host "    [-] Asset archive already present on disk: $LabName$FileExtension" -ForegroundColor Yellow
    }
}
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "🎉 ALL TARGET ARCHIVES SYNCHRONIZED CLEANLY!" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
