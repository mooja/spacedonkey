from fabric.api import *


localhost = 'localhost'
upstream_host = 'spacedonkey.org'

project_root = '/home/mooja/spacedonkey/'
app_root = '/home/mooja/spacedonkey/spacedonkey/'
python_path = "/home/mooja/envs/spacedonkey/bin/python"

env.user = 'mooja'
# env.hosts.append(upstream_host)
# env.hosts.append(localhost)


def commit():
    with cd(project_root):
        local("git commit")


def push():
    with cd(project_root):
        local("git push")


def pull():
    with cd(project_root):
        run("git pull")


def restart_webserver():
    sudo("restart spacedonkey")


def deploy():
    print("Preparing to deploy...")

    # commit & push locally
    commit()
    push()

    # pull remotely and restart server remotely
    pull()
    restart_webserver()

    print("Deployment complete.")


def load_fixtures():
    with cd(app_root):
        with settings(warn_only=True):
            if not run("test -f db.sqlite3"):
                run("rm db.sqlite3")
        run("{python_path} manage.py migrate".format(python_path=python_path))
        run("{python_path} fixtures/load.py".format(python_path=python_path))
