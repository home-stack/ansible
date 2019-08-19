#!/bin/bash

function virtual_env_check() {
  python <<EOF
import imp
try:
    imp.find_module('virtualenv')
    found = True
except ImportError:
    found = False

if not found:
    exit(1)
EOF

  if [ $? -eq 1 ]; then
    echo "Please install python's virtualenv module"
    exit
  fi
}

virtual_env_check

if [ ! -d .ansible ]; then
  virtualenv .home-stack-ansible
fi 
. ./.home-stack-ansible/bin/activate
pip install -r requirements.txt

