import mon
import pkg
from install import install, mirror_install
from uninstall import uninstall

# Allow to set some information about this distro
#

distro = None
release = None
codename = None


def choose_init():
    """
    Select a init system

    Returns the name of a init system (upstart, sysvinit ...).
    """
    return 'systemd'
