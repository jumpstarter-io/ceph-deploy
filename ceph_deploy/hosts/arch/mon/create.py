from ceph_deploy.hosts import common
from ceph_deploy.lib.remoto import process


def create(distro, args, monitor_keyring):
    logger = distro.conn.logger
    hostname = distro.conn.remote_module.shortname()
    common.mon_create(distro, args, monitor_keyring, hostname)
    systemctl = distro.conn.remote_module.which('systemctl')

    if not systemctl:
        logger.warning('could not find `systemctl` command')
        
    if distro.init == 'systemd':
        process.run(
            distro.conn,
            [
                systemctl,
                'enable',
                'ceph-mon@{hostname}'.format(hostname=hostname)
            ],
            timeout=7,
        )
        process.run(
            distro.conn,
            [
                systemctl,
                'start',
                'ceph-mon@{hostname}'.format(hostname=hostname)
            ],
            timeout=7,
        )
        
        process.run(
            distro.conn,
            [
                systemctl,
                'enable',
                'ceph-create-keys@{hostname}'.format(hostname=hostname)            
            ],
            timeout=7,
        )
        process.run(
            distro.conn,
            [
                systemctl,
                'start',
                'ceph-create-keys@{hostname}'.format(hostname=hostname)            
            ],
            timeout=7,
        )
    else:
        raise RuntimeError('create cannot use init %s' % distro.init)
