# Development Requirements

You must have VirtualBox and vagrant installed. Ensure your .ssh/config is either empty or does not contain a:

```
Host *
```

entry.

It is best to ensure the version of geerlingguy/centos7 has virtualbox extensions that match your current version of virtualbox to shorten test times.

## Install/Setup

1) run `./setup.sh`
1) activate venv with `. ./.home-stack-ansible/bin/activate`
1) Test a role. Enter roles/home-stack.base run `molecule test`
