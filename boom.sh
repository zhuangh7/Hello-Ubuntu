#!/bin/bash
set -e
python3 Hello.py
cp /etc/update-motd.d/00-header 00-header.bak
#echo 'head -n 30 /etc/update-motd.d/00-header > /etc/update-motd.d/00-header' | sudo su
echo 'head -n 30 /etc/update-motd.d/00-header > temp' | sudo su
echo 'cat out_ >> temp' | sudo su
sudo mv temp /etc/update-motd.d/00-header
sudo chmod 755 /etc/update-motd.d/00-header

