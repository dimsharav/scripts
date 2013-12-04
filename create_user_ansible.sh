#!/bin/bash

USERNAME=dimsharav
FILEPATH=/home/$USERNAME/.ssh
KEYURL=http://prk.perm.ru/files/id_rsa.pub 

sed -e "s/# %wheel/%wheel/" -i /etc/sudoers
useradd -U -m -G wheel $USERNAME
mkdir -p $FILEPATH 
wget $KEYURL
cat id_rsa.pub > $FILEPATH/authorized_keys
chown -R $USERNAME:$USERNAME $FILEPATH
chmod -R go-rwx $FILEPATH 
passwd $USERNAME
