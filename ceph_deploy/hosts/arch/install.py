from ceph_deploy.util import pkg_managers, templates
from ceph_deploy.lib.vendor.remoto import process

def install(distro, version_kind, version, adjust_repos):
    process.run(
        distro.conn,
        [
            'pacman',
            '-S',
            '--noconfirm',
            '--needed',
            'ceph',
            'gdisk'
        ],
    )

def mirror_install(distro, repo_url, gpg_url, adjust_repos):
    """ Will have to look into this since remote_module can't edit pacman.conf.
        Also this is less than desireable way to do it.
    with open('/etc/pacman.conf', 'w') as f:
        file_rows = f.readlines()
        if not any("[jumpstarter]" in s for s in file_rows):
            file_rows.append('\n')
            file_rows.append('[jumpstarter]')
            file_rows.append('SigLevel = Never')
            file_rows.append('Server = http://repo.jumpstarter.io/repo')
            f.writelines(file_rows)

    pkg_managers.pacman(distro.conn, 'wget')
    pkg_managers.pacman(distro.conn, 'ceph')
    """
    
