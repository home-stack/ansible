# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "vagrant-centos7" do |web|
    web.vm.provider "virtualbox" do |provider, override|
      provider.customize [ "guestproperty", "set", :id, "--timesync-threshold", 10000 ]
      override.vm.box = "geerlingguy/centos7"
      # Disable the default portmap for ssh in case there are multiple vagrant based VMs
      # and then manually set the port
      # Provide access to mysql to make root appear to come from "gateway" making
      # permissions easy

      provider.memory = "2048"
      provider.cpus = "2"
    end
    web.vm.synced_folder ".", "/vagrant", disabled: true
  end
end
