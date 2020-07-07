import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_lsyncd_is_installed(host):
    package = host.package("lsyncd")
    assert package.is_installed
    assert package.version.startswith("2.2")


def test_lsyncd_running_and_enabled(host):
    service = host.service("lsyncd")
    assert service.is_running
    assert service.is_enabled


def test_lsyncd_config(host):
    lsyncd_conf = host.file('/etc/lsyncd.conf')
    assert 'root' == lsyncd_conf.user
    assert 0o644 == lsyncd_conf.mode
