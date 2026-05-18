# Active Directory Lab Range Setup & Fuzzing Deployment Blueprint
Comprehensive documentation for provisioning an isolated Windows Server 2025 target range optimized for fuzzing and Active Directory exploitation frameworks on a Windows 11 Home host machine.

## ??? Phase 1: Host System Configuration (Windows 11 Home)
- Toggle **Memory Integrity** to **OFF** to release exclusive VT-x hooks.
- Expose Guest Hypervisor API Support: Enable-WindowsOptionalFeature -Online -FeatureName "HypervisorPlatform" -All

## ?? Phase 2: Windows Server 2025 Provisioning
- **OS Layout Configuration:** Fresh Windows Server 2025 Standard Evaluation (Desktop Experience) on unified Disk 0 unallocated partition block.

## ?? Phase 3: Active Directory Domain Services (AD-DS) Promotion
- Graphically provisioned forest infrastructure under localized realm tree root 	rapped.local with automated catalog zones.
