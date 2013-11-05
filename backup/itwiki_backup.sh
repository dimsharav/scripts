#!/bin/sh

# Бэкап dokuwiki с mars.prk.local
# ===============================
#
# Зависимости:
#   - sshfs
#   - настроенная авторизация по ключам

REMOTE_SERVER="192.168.0.4"
REMOTE_DIR="/var/data"
MOUNT_DIR="/media/net/mars/www"
BACKUP_DIR="/media/net/uranus/e/backup/mars"
BACKUP_DATE=$(date +%Y-%b-%d--%k_%M_%S)

mkdir -p MOUNT_DIR

sshfs $REMOTE_SERVER:$REMOTE_DIR $MOUNT_DIR

tar zcf $BACKUP_DIR/itwiki.$BACKUP_DATE.tar.gz $MOUNT_DIR/dokuwiki/
