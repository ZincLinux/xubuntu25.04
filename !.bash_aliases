alias ytmp3='cd ~/Music&& yt-dlp --ignore-errors --restrict-filenames --console-title --extract-audio --audio-format mp3 --embed-thumbnail'
alias yt240="yt-dlp -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=240]+bestaudio/best'"
alias yt360="yt-dlp -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=360]+bestaudio/best'"
alias yt720="yt-dlp -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=720]+bestaudio/best'"
alias yt1080="yt-dlp -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=1080]+bestaudio/best'"
alias ytmax='yt-dlp -i -4 --restrict-filenames --console-title'

alias yts240="yt-dlp --write-subs --write-auto-subs --sub-langs="en.*,en" -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=240]+bestaudio/best'"
alias yts360="yt-dlp --write-subs --write-auto-subs --sub-langs="en.*,en" -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=360]+bestaudio/best'"
alias yts720="yt-dlp --write-subs --write-auto-subs --sub-langs="en.*,en" -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=720]+bestaudio/best'"
alias yts1080="yt-dlp --write-subs --write-auto-subs --sub-langs="en.*,en" -i -4 --restrict-filenames --console-title -f 'bestvideo[height<=1080]+bestaudio/best'"
alias ytsmax="yt-dlp --write-subs --write-auto-subs --sub-langs="en.*,en" -i -4 --restrict-filenames --console-title"

alias UpdateSystem='sudo apt update&& sudo apt upgrade -y&& sudo apt autoremove -y&& sudo yt-dlp -U'