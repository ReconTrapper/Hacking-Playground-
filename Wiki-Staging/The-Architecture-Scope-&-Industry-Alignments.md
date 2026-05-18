# The Architecture Scope & Industry Alignments

This multi-OS laboratory is an advanced, infrastructure-as-code cyber security range engineered to simulate real-world corporate vulnerabilities, air-gapped sandbox environments, and automated data logging frameworks.

---

## 🏗️ Core Laboratory Capabilities

### 1. High-Density Enterprise Emulation Matrix (`trapped.local`)
* **Infrastructure**: Windows Server 2025 Standard Evaluation Active Directory Domain Services (AD-DS) Forest.
* **Target Density**: Exactly **2,491 active fuzzed user profiles**, tiered Organizational Unit (OU) maps, and nested group structures committed straight to the underlying NTDS database.
* **Vulnerability Vectors**: Pre-configured with intentional corporate flaws, including Service Principal Name (SPN) mappings and pre-authentication requirements disabled for active **AS-REP Roasting** training.

### 2. Multi-OS Lightweight Target Catalog
* **DC-1 Target (`DC_1_Target`)**: Linux-based appliance running a vulnerable **Drupal CMS core software** stack optimized for Remote Code Execution (RCE) and web application enumeration.
* **SickOs 1.1 Target (`SickOs_1_1`)**: Dedicated intermediate boot-to-root platform built for exploiting proxy server misconfigurations and practicing shell hunting.
* **Kioptrix Level 1 Target (`Kioptrix_Level_1`)**: Legacy Linux node mapping out ancient SMB, Apache, and OpenSSL daemon vulnerabilities. Hard-locked to VirtualBox IDE drive controllers to bypass legacy kernel panics.

### 3. Cross-Platform Loot Management Automation (`Add-Loot.ps1`)
* **Infrastructure**: A native Linux-PowerShell Core 7 orchestration tool that bridges your terminal directly with your local encrypted password vault database (**KeePassXC**).
* **Execution**: Dynamically prompts for target nodes (1–4), maps static IP ranges in memory, and pipes cleartext credentials straight into your local, air-gapped `.kdbx` file structure via the `keepassxc-cli` backend wrapper.

---

## 📈 Industry Benchmarks & Technical Alignments

If you are exploring the field of Cyber Range Engineering or DevSecOps, this laboratory architecture directly mirrors the design patterns found in major open-source testing projects:

* 🌲 **GOAD (Game of Active Directory)**: Aligns with our automated domain generation loops. GOAD uses Vagrant and Ansible to provision multi-domain forests with cascading flaws.
* 🛡️ **Detection Lab**: Aligns with our hypervisor sandboxing methods. Detection Lab automates building AD domains alongside defensive blue-team logging infrastructures like Splunk and Sysmon.
* 🤖 **Automated Lab**: Aligns with our core PowerShell infrastructure design. Automated Lab is a native Windows scripting module designed to deploy complex multi-machine ranges entirely unattended.