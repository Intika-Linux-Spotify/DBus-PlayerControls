import subprocess
import sys
if  sys.argv[1] == "playpause": 
	if subprocess.Popen("lsof -wc mocp | awk \'$4~\"[0-9]r\" && $5==\"REG\"' | grep -o \'[^/]*$\'", shell=True, stdout=subprocess.PIPE).stdout.read() != b'':
		subprocess.Popen("mocp -G", shell=True)
	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Paused\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play", shell=True)

	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Playing\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause", shell=True)

elif  sys.argv[1] == "prev":
	if subprocess.Popen("lsof -wc mocp | awk \'$4~\"[0-9]r\" && $5==\"REG\"' | grep -o \'[^/]*$\'", shell=True, stdout=subprocess.PIPE).stdout.read() != b'':
		subprocess.Popen("mocp -r", shell=True)
	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Paused\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous", shell=True)
	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Playing\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous", shell=True)

elif  sys.argv[1] == "next":
	if subprocess.Popen("lsof -wc mocp | awk \'$4~\"[0-9]r\" && $5==\"REG\"' | grep -o \'[^/]*$\'", shell=True, stdout=subprocess.PIPE).stdout.read() != b'':
		subprocess.Popen("mocp -f", shell=True)
	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Paused\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next", shell=True)
	elif subprocess.Popen("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus", shell=True, stdout=subprocess.PIPE).stdout.read() == b'Playing\n':
		subprocess.Popen("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next", shell=True)
