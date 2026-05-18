# 🏗️ Multi-Target Penetration Testing & Active Directory Lab Range

An advanced, infrastructure-as-code hacking playground engineered to deploy, provision, and audit an isolated multi-system target range inside a sandboxed hypervisor network.

## 🎯 Active Lab Range Ecosystem

This playground hosts multiple distinct target platforms and testing matrices configured across an isolated network segment (**LabNet / 10.0.2.0/24**):

### 1. 🌲 Windows Server 2025 Domain Controller (	rapped.local)
* **IP Address:** Dynamic DHCP (10.0.2.8)
* **Status:** Fully operational AD-DS forest.
* **Fuzzing Architecture:** Aggressively populated with **2,500+ randomized fuzzing objects** (OUs, Users, Groups, and complex ACL maps) via the BadBlood framework to simulate a realistic enterprise network.

### 2. 🌐 DC-1 Web Target Application
* **IP Address:** Static (10.0.2.5)
* **Status:** Active Drupal web application instance.
* **Testing Matrix:** Used to practice web exploitation vectors, content management system (CMS) enumeration, and local privilege escalation.

### 🐧 3. Kioptrix Level 1 Legacy Target
* **Status:** Active legacy boot-to-root testing target.
* **Storage Optimization:** Remapped to a custom Controller: IDE architecture to securely bypass legacy SATA kernel panics.
* **Testing Matrix:** Focused on legacy SMB vulnerability exploitation, configuration weaknesses, and basic network enumeration.

---

## 🗺️ Repository Directory Structure
* 📂 **01-Hypervisors/**: Baseline configurations, Hyper-V/Core Isolation alignment configurations, and platform settings.
* 📂 **02-ISO-Archive/**: Storage architecture maps for operating system evaluation images.
* 📂 **03-Active-VMs/**: Staging ranges for isolated network nodes (Kali-Control/, Meta-Target/, Web-Target/, Windows-Lab/).
* 📂 **04-Source-Code/**: Production-ready scripts including:
  * [Provision-Lab-Domain.ps1](./04-Source-Code/Provision-Lab-Domain.ps1): Automated AD-DS deployment scripts.
  * [AD-DS-Lab-Setup.md](./04-Source-Code/AD-DS-Lab-Setup.md): Deep technical system setup blueprints.
  * Recon-Scanners/: Custom Python tools including ping_sweeper.py.

---
*Maintained globally by **ReconTrapper**. Developed exclusively for advanced offensive and defensive security research.*