#!/bin/bash

ssh-keygen -t rsa -b 4096
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
git config --global user.email $1
git config --global user.name $2
cat /root/.ssh/id_rsa.pub
