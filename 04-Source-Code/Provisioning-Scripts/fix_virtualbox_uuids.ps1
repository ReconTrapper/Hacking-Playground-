<#
.SYNOPSIS
    Fixes VirtualBox VM shell configuration registration collisions.
#>
$VboxPath = "C:\VMs\kali-linux-2026.1-virtualbox-amd64 (1)\kali-linux-2026.1-virtualbox-amd64\kali-linux-2026.1-virtualbox-amd64.vbox"
if (Test-Path $VboxPath) {
    $NewVmUuid = [Guid]::NewGuid().ToString()
    (Get-Content $VboxPath) -replace 'Machine uuid="\{[a-f0-9\-]+\}"', "Machine uuid=`"{$NewVmUuid}`"" | Set-Content $VboxPath
    & "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" registervm $VboxPath
    Write-Host "[+] VirtualBox shell identifier patch applied successfully." -ForegroundColor Green
} else {
    Write-Warning "Target .vbox configuration file not found at path."
}
