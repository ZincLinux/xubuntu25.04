!#/bin/bash
# edit file as desired. see: README

# remove Apport, Snaps
sudo apt purge -y snapd apport*&& sudo apt update

# enable librewolf via extrepo
sudo apt install extrepo -y&& extrepo enable librewolf&& sudo apt update

# xfce4 & fonts & 'core' apps
sudo apt install -y caffeine engranpa mpv orage thunar-archive-plugin xfce4-timer-plugin xfce4-panel-profiles hack mononoid baobab blanket feathernotes galculator krita gimp gparted gthumb inkscape librewolf mousepad redshift-gtk system-config-printer usb-creator-gtk zulucrypt yt-dlp

# games
sudo apt install -y aisleriot gnome-sudoku gweled

# deps: brogue-ce/sonagets
sudo apt install -y libsdl2-2.0-0 libsdl2-image-2.0-0 python3-tk python3-pil.imagetk

# ytdlp dl/install from git ... remove from apt if used.
#wget 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux'&& #chmod +x yt-dlp_linux&& sudo ./dlp_linux&& rm yt-dlp_linux

# docklike plugin dl/install 
wget 'https://mxrepo.com/mx/repo/pool/main/x/xfce4-docklike-plugin/xfce4-docklike-plugin_0.4.1-0.1~mx23+1_amd64.deb'&& sudo dpkg --install xfce4-docklike-plugin_0.4.1-0.1~mx23+1_amd64.deb&& rm xfce4-docklike-plugin_0.4.1-0.1~mx23+1_amd64.deb

# vscodium dl/install
#wget 'https://github.com/VSCodium/vscodium/releases/download/1.96.2.24355/codium_1.96.2.24355_amd64.deb'
#sudo dpkg --install codium_1.96.2.24355_amd64.deb
#rm codium_1.96.2.24355_amd64.deb

