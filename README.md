# CTData CKAN Ansible Playbooks

## Getting Started

These ansible playbooks will install the latest version of CKAN on to a Vagrant virtual machine or a remote server.

You will first need to install Virtualbox and Vagrant. On OS X, you should install via Homebrew:

`$ brew cask install virtualbox`

followed by

`$ brew cask install vagrant`

You will then need to install Ansible locally via `pip install ansible`. I would recommend installing ansible within a virtual environment in to which you clone this repository.

To start with initial CKAN development, create the virtual machine and run the playbooks with `vagrant up` from the root directory. Go get a cup of coffee. This should run for 10 minutes or so while it installs server dependencies and the ckan files.

Once complete, you should be able to visit `http://192.168.33.15/` in your browser and see the basic CKAN application up and running.

At this point you can start interacting with CKAN. Consult the CKAN sysadmin guide for instructions on how to manage accounts, etc. Consult the developer's guide to see how to start customizing CKAN.

To access the vagrant machine via ssh, you can run `vagrant ssh`. If you want to copy files to and from the machine (you should generally not do this and instead should configure Ansible to do the file setup but you might need to do something temporarily in order to troubleshoot), you should install `vagrant-scp` with `vagrant plugin install vagrant-scp`.
