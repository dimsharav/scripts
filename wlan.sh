#!/bin/sh
ip addr add 10.0.169.2/24 dev wlan0
ip addr add 10.0.167.3/24 dev ext
ip link set up ext
systemctl start dnsmasq.service
