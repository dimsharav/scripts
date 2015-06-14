#!/bin/sh
VBoxManage controlvm spcwrks savestate
VBoxManage controlvm debian savestate
VBoxManage controlvm SVPN savestate
