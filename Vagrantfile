  # -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.network :private_network, ip: "192.168.33.15"

  # config.vm.provider :virtualbox do |vb|
  #   vb.customize ["modifyvm", :id, "--name", "ckan", "--memory", "2048"]
  # end
  # Provide an absolute path to the ckan extension directory that is being developed. 
  config.vm.synced_folder "../ctdata-ckan-theme-v2", "/home/vagrant/theme"
  config.ssh.forward_agent = true


  # Ansible provisioner.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant.yml"
    ansible.host_key_checking = false
    ansible.ask_vault_pass = false
    ansible.verbose = "vvvv"
  end

  config.vm.provision "resume", type: "ansible" do |resume|
    resume.playbook = "vagrant.yml"
    resume.limit = "@vagrant.retry"
    resume.host_key_checking = false
    resume.ask_vault_pass = false
    resume.verbose = "vvvv"
  end
end
