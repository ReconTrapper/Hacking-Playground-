# ??? Automated Active Directory Range & Fuzzing Playground

An advanced, infrastructure-as-code hacking playground engineered to deploy, provision, and audit an isolated Active Directory Domain Services (AD-DS) network range inside a sandboxed hypervisor sandbox environment.

## ?? Project Overview
This repository hosts the automation scripts, provisioning blueprints, and architectural document guides used to spin up a fully operational **Windows Server 2025** Enterprise Domain Controller. The environment is aggressively populated with over **2,500+ randomized fuzzing objects** via the BadBlood framework to simulate a realistic, dense enterprise target network for security auditing, penetration testing, and defensive engineering.

## ??? Repository Structure
- **?? 01-Hypervisors/**: Baseline configurations and platform settings for low-level Type-2 virtualization.
- **?? 02-ISO-Archive/**: Storage architecture maps for operating system evaluation images.
- **?? 03-Active-VMs/**: Staging ranges for isolated network nodes (Kali, Active Directory, Web Targets).
- **?? 04-Source-Code/**: Production-ready [PowerShell Automation Scripts](./04-Source-Code/Provision-Lab-Domain.ps1) and deep [Technical Setup Blueprints](./04-Source-Code/AD-DS-Lab-Setup.md).

## ?? Quick Navigation
- **Detailed Build Documentation**: Read the full step-by-step engineering journey in our [Lab Setup Guide](./04-Source-Code/AD-DS-Lab-Setup.md).
- **Interactive Knowledge Base**: Check out the live project [Wiki Ecosystem](https://github.com).

---
*Maintained by **ReconTrapper**. Developed exclusively for advanced offensive and defensive security research.*
