#!/usr/bin/env bash

apt update
apt-get install -y python python-pip python-dev python3 python3-pip python3-dev

pip install subprocess32 gradescope-utils numpy scipy
pip3 install gradescope-utils numpy scipy hypothesis