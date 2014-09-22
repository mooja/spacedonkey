from fabric.api import *
from fabric.contrib.console import confirm


localhost = 'localhost'
upstream_host = 'spacedonkey.org'

project_root = '/home/mooja/spacedonkey/'
app_root = '/home/mooja/spacedonkey/spacedonkey/'
python_path = "/home/mooja/envs/spacedonkey/bin/python"

env.user = 'mooja'
# env.hosts.append(upstream_host)
# env.hosts.append(localhost)


def commit():
    with settings(warn_only=True):
        with cd(project_root):
            r = local("git commit")
            if r.failed and not confirm("Commit is not clearn failed. Continue?"):
                abort()


def push():
    with cd(project_root):
        local("git push")


def pull():
    with cd(project_root):
        run("git pull")


def restart_webserver():
    sudo("restart spacedonkey")


def collectstatic():
    with cd(app_root):
        run("{python_path} manage.py collectstatic".format(python_path=python_path))


def deploy():
    print("Preparing to deploy...")

    # commit & push locally
    commit()
    push()

    # pull remotely and restart server remotely
    pull()
    collectstatic()
    restart_webserver()

    print("Deployment complete. Mathematical!")


def fixtures():
    with cd(app_root):
        with settings(warn_only=True):
            if not run("test -f db.sqlite3"):
                run("rm db.sqlite3")
        run("{python_path} manage.py migrate".format(python_path=python_path))
        run("{python_path} fixtures/load.py".format(python_path=python_path))
