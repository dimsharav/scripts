#!/bin/bash
for ((a = 102; a <= 114; a++)); do; ssh 192.168.0.115 -t sudo shutdown -h now; done
