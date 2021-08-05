import subprocess
import os

def convert(in_file, out_file):
	cmd = "ffmpeg -i " + in_file + ' -vn -ab 128k -ar 44100 -y ' + out_file
	subprocess.run(cmd)

in_file = input("Введи файл: ")
base, ext = os.path.splitext(in_file)

if ext == "":
	ext=".webm"
	in_file=base+ext

out_file = base + '.mp3'
convert(in_file, out_file)

input()