import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_database_running_and_enabled(host):
    database = host.service("mariadb")
    assert database.is_running
    assert database.is_enabled
