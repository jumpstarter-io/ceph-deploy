from ceph_deploy.util import pkg_managers
from ceph_deploy.lib.vendor.remoto import process


def uninstall(conn, purge=False):
    packages = [
        'ceph'
        ]
    pkg_managers.pacman_remove(
        conn,
        packages,
        purge=purge,
    )
