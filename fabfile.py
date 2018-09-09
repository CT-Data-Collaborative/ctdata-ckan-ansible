from fabric.api import env, local, run
# TODO Change these commands to use Linode

def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    env.hosts = ['127.0.0.1:2222']

    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


def uname():
    run('uname -a')

def ckan_logs(lines=50):
    run('sudo tail -n%s /var/log/apache2/ckan_default.error.log' % lines)

def vagrant_deploy():
    local(
        "ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --ask-vault-pass --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant vagrant.yml --tags 'deploy'")

def ec2_deploy():
    local(
        "ansible-playbook -i development --ask-vault-pass -vvvv --private-key=~/.ssh/pems/ctdata-dev.pem webservers.yml --tags 'deploy'")

def ec2_build():
    local(
        "ansible-playbook --ask-vault-pass -vvvv --private-key=~/.ssh/pems/ctdata-dev.pem -i development webservers.yml")
