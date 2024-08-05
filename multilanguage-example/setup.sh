#!/bin/bash
# install any software required (Ubuntu)
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
add-apt-repository main
add-apt-repository universe
add-apt-repository restricted
add-apt-repository multiverse
apt-get update
apt-get install -y python3 python3-pip python3-dev build-essential valgrind git netpbm libnetpbm10-dev \
  clang software-properties-common libsigsegv2 libsigsegv-dev libjpeg-dev libjpeg-progs lua5.3

# install python libraries
pip3 install gradescope-utils numpy scipy hypothesis

# install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
