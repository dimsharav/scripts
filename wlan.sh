#!/bin/sh
ip addr add 10.0.169.2/24 dev wlan0
systemctl start dnsmasq.service
