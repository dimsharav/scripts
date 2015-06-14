#!/bin/sh
VBoxManage startvm spcwrks --type headless
VBoxManage startvm debian --type headless
VBoxManage startvm SVPN --type headless
