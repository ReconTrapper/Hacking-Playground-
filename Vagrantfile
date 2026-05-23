# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  # TARGET 1: Automated Windows Server 2025 Domain Controller
  config.vm.define "windows_server" do |srv|
    srv.vm.box = "opentable/win-2025-standard"
    srv.vm.hostname = "Windows-Server-Target"
    srv.vm.network "private_network", ip: "10.0.2.8", virtualbox__intnet: "LabNet"
    
    config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096|config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096|config.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = 4096
      config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096.customize ["modifyvm", :id, "--vram", "128"]
      config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
    end
    srv.vm.provision "shell", path: "04-Source-Code/Provision-Lab-Domain.ps1"
  end

  # TARGET 2: Automated Kali Linux Attacker Controller Node
  config.vm.define "kali_attacker" do |kali|
    kali.vm.box = "kalilinux/kali-linux"
    kali.vm.hostname = "Kali-Control"
    kali.vm.network "private_network", ip: "10.0.2.3", virtualbox__intnet: "LabNet"
    
    config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096|config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096|
      config.vm.provider "virtualbox" do |vb|vb.cpus = 2vb.memory = 4096.memory = 2048
    end
    kali.vm.provision "shell", inline: "echo 'nameserver 10.0.2.8' > /etc/resolv.conf"
  end
end
