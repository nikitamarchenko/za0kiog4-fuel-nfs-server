__author__ = 'nmarchenko'

from fabric.api import local, run, env, put, prefix

FUEL_VM = 'fuel'

env.hosts = ['root@{}'.format(FUEL_VM)]


def init():
    local('ssh-keygen -f "/home/nm/.ssh/known_hosts" -R {}'.format(FUEL_VM))
    local('ssh-keygen -f "/home/nm/.ssh/known_hosts" -R 10.20.0.2')
    local('ssh-copy-id -i ~/.ssh/id_rsa.pub root@{}'.format(FUEL_VM))
    run('yum install nano htop -y')
    run('mv /etc/fuel/client/config.yaml ~/.config.yaml')
    run('echo "export FUELCLIENT_CUSTOM_SETTINGS=/root/.config.yaml" >> .bashrc')

def build():
    local('fpb --build .')

def install():
    put('za0kiog4-1.0-1.0.0-1.noarch.rpm', '/root/')
    run('fuel plugins --install za0kiog4-1.0-1.0.0-1.noarch.rpm')
    run('rm za0kiog4-1.0-1.0.0-1.noarch.rpm')
    local('rm za0kiog4-1.0-1.0.0-1.noarch.rpm')

def uninstall():
    run('fuel plugins --remove za0kiog4==1.0.0')

def rebuild():
    build()
    uninstall()
    install()
