import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chronyd_running_and_enabled(host):
    chronyd = host.service("chronyd")
    assert chronyd.is_running
    assert chronyd.is_enabled
