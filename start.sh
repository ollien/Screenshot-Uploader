dir=/Volumes/Backroom/ScreenshotsUp/

fswatch --print0 -e '/\.' $dir | xargs -0 -n1 ./client.py