#!/usr/bin/env bash
set -euo pipefail
LAB_ROOT="${HOME}/Hacking-Playground"

echo "===================================================="
echo "🚀 INITIALIZING LINUX/KALI LAB PROVISIONING SUITE"
echo "===================================================="

DIRECTORIES=(
    "${LAB_ROOT}/01-Hypervisors"
    "${LAB_ROOT}/02-ISO-Archive/Linux"
    "${LAB_ROOT}/02-ISO-Archive/Windows"
    "${LAB_ROOT}/03-Active-VMs/Kali-Control"
    "${LAB_ROOT}/03-Active-VMs/Meta-Target"
    "${LAB_ROOT}/03-Active-VMs/Web-Target"
    "${LAB_ROOT}/03-Active-VMs/Windows-Lab"
    "${LAB_ROOT}/04-Source-Code/Recon-Scanners"
    "${LAB_ROOT}/04-Source-Code/Web-Exploitation"
    "${LAB_ROOT}/04-Source-Code/Audit-Utilities"
    "${LAB_ROOT}/04-Source-Code/Provisioning-Scripts"
)

for dir in "${DIRECTORIES[@]}"; do
    if [ ! -d "${dir}" ]; then
        mkdir -p "${dir}"
        echo "   [+] Provisioned: ${dir}"
    else
        echo "   [-] Exists: ${dir}"
    fi
    touch "${dir}/.gitkeep"
done
echo -e "\n[🎉] Complete! Workspace initialized cleanly."
