# 🚀 What Happens During Deployment

When a user runs the Quick Deployment commands, the system automates the creation of an isolated sandbox environment through the following steps:

### 🛠️ Automated Tool Installation
* Uses Windows Package Manager (winget) to silently install HashiCorp Vagrant.
* Bypasses prompts by automatically accepting all vendor source and package agreements.

### 📦 Source Code Retrieval
* Clones the active laboratory source files and configuration assets directly from the remote repository.

### 📂 Workspace Initialization
* Drops the user's administrative command terminal directly into the root deployment folder (Hacking-Playground-).

### ⚙️ Automated Lab Provisioning (agrant up)
* **Box Download**: Fetches the required pre-configured operating system images if not already cached on the host.
* **Virtualization Launch**: Boots up the exact instances and nodes specified by the workspace topology.
* **Isolated Networking**: Establishes secure private networks, static IP routing, and host-only adapters to ensure no malicious traffic escapes to the local home network.
* **Environment Provisioning**: Executes background shell scripts to auto-install hacking tools, compile target vulnerabilities, and set up the active lab scenarios.