# Cross-Platform Loot & Password Vault Automation Framework

To systematically log credentials, root keys, and hashes discovered across your multi-OS testing catalog without manual text document fatigue, utilize our local automation tool chain.

## ⚙️ Automated Integration Logic
The script asking you which system you successfully compromised, maps the static lab network IP routing values dynamically, and passes encrypted execution variables securely to `keepassxc-cli` to index your data in real-time.

```powershell
# Execute natively on Kali Linux by loading the PowerShell core extension wrapper
pwsh ./04-Source-Code/Add-Loot.ps1
```

## 📂 Vault Security Categories Managed
* 🌲 **`Active Directory Range`** ➡️ Targeted parameters tracking fuzzed corporate user matches on `10.0.2.8`.
* 🌐 **`Web Application Targets`** ➡️ Logging CMS administrative access routes cracked on DC-1 (`10.0.2.5`) or SickOs (`10.0.2.11`).
* 🔑 **`Domain Admins / Loot`** ➡️ Holding persistent Golden Ticket credentials or Linux high-privilege root access strings (`10.0.2.12`).
