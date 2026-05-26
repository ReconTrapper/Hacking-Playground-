# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  # =====================================================================
  # 🌲 TARGET 1: LINKED WINDOWS SERVER 2025 DOMAIN CONTROLLER
  # =====================================================================
  config.vm.define "windows_server" do |srv|
    srv.vm.box = "gusztavvargadr/windows-server-2025-standard"
    srv.vm.hostname = "Windows-Server-Target"
    srv.vm.network "private_network", ip: "10.0.2.8", virtualbox__intnet: "LabNet"
    
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = 4096  
      vb.customize ["modifyvm", :id, "--vram", "128"]
      
      # CONGRUENCE LINK: Tells VirtualBox to store the active hard drive 
      # files inside your centralized production storage cage directory!
      vb.customize ["modifyvm", :id, "--snapshotfolder", "C:/Hacking-Playground/03-Active-VMs/Windows-Lab"]
    end
    
    # CONGRUENCE LINK: Reaches back into your main repository to execute 
    # your production code without maintaining duplicate copies of the file!
    srv.vm.provision "shell", path: "../Hacking-Playground/04-Source-Code/Provision-Lab-Domain.ps1"
  end

  # =====================================================================
  # 📟 TARGET 2: LINKED WEAPONIZED KALI LINUX ATTACK CONTROLLER NODE
  # =====================================================================
  config.vm.define "kali_attacker" do |kali|
    kali.vm.box = "kalilinux/kali-linux"
    kali.vm.hostname = "Kali-Control"
    kali.vm.network "private_network", ip: "10.0.2.3", virtualbox__intnet: "LabNet"
    kali.vm.network "public_network", type: "dhcp"
    
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = 2048
    end
  end
end