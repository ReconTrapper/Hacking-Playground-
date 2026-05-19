# Hardware Compatibility & System Resource Adaptation Matrix

Because The Killbox: Trapper Range is built on flexible, code-driven virtualization principles, it can be dynamically scaled and adapted to run across a wide range of host hardware configurations.

---

## 💻 Hardware Performance Profiles

### 1. The Minimal Profile (For 8GB RAM / 4-Core Laptops)
* **The Adaptation Strategy**: Run an **isolated 1-on-1 testing track**. Users should boot only the Kali Linux controller VM alongside a single target node at any given time.
* **Resource Mapping**: Allocate 2GB RAM to Kali Linux and 3GB RAM to the Windows Server 2025 Domain Controller. This utilizes 5GB of virtual memory pool space, leaving a safe 3GB buffer for the Windows 11 host operating system to prevent kernel exhaustion or crashing.

### 2. The Recommended Profile (For 16GB RAM / 6+ Core Laptops)
* **The Adaptation Strategy**: Run **full-spectrum corporate network simulation**. Users can safely boot and maintain the entire target catalog simultaneously to practice multi-system pivoting and lateral movement.
* **Resource Mapping**: Allocate 2GB RAM to Kali Linux, 4GB RAM to the Windows Server 2025 Domain Controller, and 1GB RAM to the DC-1 Web Application node. This configuration utilizes 7GB of virtual memory pool space, allowing full concurrent testing while the host machine remains perfectly responsive.

---

## 💾 Storage & Hypervisor Footprint
* **Solid State Drive (SSD) Allocation**: Testers require roughly **30GB to 40GB of free local storage space** to comfortably download, extract, and cache the virtual hard disk images (`.vdi` and `.vmdk` files).
* **Paravirtualization Driver Core Line**: Ensure VirtualBox settings map processing traffic cleanly through the native Windows Hypervisor Platform (WHv) paravirtualization interface interface. This guarantees high-speed guest performance while keeping **Windows 11 Core Isolation / Memory Integrity active** on the host.