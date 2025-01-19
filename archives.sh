#!/bin/bash

# get true user, this script should be called by sudo.
USER=$(id -un)
if [ "$USER" = "root" ] && [ -n "$SUDO_USER" ]; then
    USER=$SUDO_USER
fi
echo "Original user: $USER"

# local-user/skel
cp .bash_aliases /home/$USER/
cp fn.conf /home/$USER/.config/feathernotes/

tar -xjf BrogueCE-linux.tar.bz2 -C /opt/
tar -xjf Telegram.tar.bz2 -C /opt/

cp sonagets /usr/bin/
cp sonagetsgui.py /usr/bin/
cp sonagetsgui.png /usr/share/icons/

cp bell.wav /opt/
cp timer.sh /opt/
cp zl25.04-panel.tar.bz2 /usr/share/xfce4-panel-profiles/layouts/
cp brogue.desktop /usr/share/applications/