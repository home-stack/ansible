import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('compute1')


def test_chronyd_correct_configuration(host):
    chronyd = host.service("chronyd")
    assert chronyd.is_running
    assert chronyd.is_enabled
