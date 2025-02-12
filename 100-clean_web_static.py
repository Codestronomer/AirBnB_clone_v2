#!/usr/bin/python3
"""This module deletes out-of-date archives, using the function do_clean"""
from fabric.api import local, run, put, env
import os


env.hosts = ['3.238.197.27', '107.21.43.52']
env.user = 'ubuntu'


def do_pack():
    """
        Creates a .tgz archive from all files in web_static folder
        Archive name:
            web_static_<year><month><day><hour><minute><second>.tgz
        Returns:
            archive path if successful else None
    """
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    return None


def do_deploy(archive_path):
    """
        Uploads an archive to web servers
        Returns:
            True if operations succeed
            False if archive_path doesn't exist or fail
    """
    import os

    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    filename = archive_path[9:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename
    if not run('mkdir -p {}'.format(foldername)).succeeded:
        return False
    if not run('tar -xzf {} -C {}'.format(filename, foldername)).succeeded:
        return False
    if not run('rm {}'.format(filename)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(foldername,
                                              foldername)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(foldername)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        foldername)).succeeded


def deploy():
    """
        Packs and deploys an archive to servers
    """
    path = do_pack()
    if path is False:
        return False
    return do_deploy(path)


def do_clean(number=0):
    """Deletes out-of-date archives of the static files.
    Args:
        number (Any): The number of archives to keep.
    """
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
