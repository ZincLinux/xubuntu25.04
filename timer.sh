#!/bin/bash
# NEEDS: aplay notify-send xfce4-timer-plugin + bell.wav
# Used as XFCE4 "Pomodoro" Timer plugin, via Timer Command. 

if [ $# -lt 2 ]; then
  echo "Usage: $0 <title> <text>"
  exit 1
fi

title="$1"
text="$2\n\nTo edit countdown, title or text: Right-click panel timer & select 'Properties.'"

mpv /opt/bell.wav&
notify-send -t 5000 -i xfce4-timer-plugin -u critical "$title" "$text"
