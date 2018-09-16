# CTData CKAN Ansible Playbooks

## Getting Started

These ansible playbooks will install the latest version of CKAN on to a Vagrant virtual machine or a remote server.

To start with initial development, create the virtual machine and run the playbooks with `vagrant up` from the root directory. Go get a cup of coffee. This should run for 10 minutes or so while it installs server dependencies and the ckan files.

Once complete, you should be able to visit `http://192.168.33.15/` in your browser and see the basic CKAN application up and running.

At this point you can start interacting with CKAN. Consult the CKAN sysadmin guide for instructions on how to manage accounts, etc. Consult the developer's guide to see how to start customizing CKAN.
