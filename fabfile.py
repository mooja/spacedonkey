from fabric.api import *


env.hosts.append('mooja@spacedonkey.org')
env.user = 'mooja'
local_root = '/home/mooja/spacedonkey_project/spacedonkey'
remote_root = '/home/mooja/spacedonkey'

def commit():
    with settings(warn_only=True):
        local("git commit -p")


def push():
    local("git push")


def upstream_restart_webserver():
    sudo("restart spacedonkey")


def upstream_pull():
    with cd("/home/mooja/spacedonkey"):
        run("git pull")


def deploy():
    # commit localy
    with lcd(local_root):
        commit()
        push()

    # pull and restart web server remotely
    with cd(remote_root):
        upstream_pull()
        upstream_restart_webserver()

    print("Deployment complete.")
