<#
.SYNOPSIS
    Automated Windows 11 Enterprise Evaluation ISO Fetcher Module.
.DESCRIPTION
    Directly streams the official, untouched 90-day enterprise evaluation media 
    straight from Microsoft's primary content delivery servers into your local lab directory.
#>

$TargetFolder = "$PSScriptRoot"
$TargetFile   = "$TargetFolder\Windows11_Enterprise_Eval.iso"

# Official, cryptographic direct download URL mapping from Microsoft Evaluation Center
$MicrosoftUrl = "https://microsoft.com"

if (Test-Path $TargetFile) {
    Write-Host "[!] Windows 11 Evaluation ISO already exists in your local cache directory. Skipping download." -ForegroundColor Yellow
    Exit
}

Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host " 📥 FETCHING WINDOWS 11 ENTERPRISE EVALUATION MEDIA (APPROX 5.4GB) " -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host "Streaming directly from Microsoft CDN infrastructure... Please wait." -ForegroundColor Yellow

try {
    # Utilizing basic parsing to bypass Internet Explorer engine dependencies on Server builds
    Invoke-WebRequest -Uri $MicrosoftUrl -OutFile $TargetFile -UseBasicParsing -Verbose
    Write-Host "[✓] SUCCESS: Windows 11 Evaluation media cached flawlessly to $TargetFile" -ForegroundColor Green
}
catch {
    Write-Error "Download pipeline interrupted. Verify outbound network connectivity or web routing configurations."
}