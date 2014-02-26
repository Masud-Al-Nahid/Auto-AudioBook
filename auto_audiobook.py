#!/usr/bin/python2.7

import ConfigParser
import os
import shutil
import subprocess

blank_lines = 0
text_lines  = 0
audio_text  = []

# Read values from an configuration file
# This file also has values written out to it at various times which is probably not the best 
# idea, but I liked the succinctness of it
INI_FILE = 'auto_audiobook.ini'
Config = ConfigParser.ConfigParser()
Config.read(INI_FILE)

# Open the book and read it in
f = open(Config.get('Book', 'Directory') + '/' + Config.get('Book', 'File'), 'r')
book = f.read().split('\n')
f.close()

# Loop through the book until we find enough non-blank lines, accumulating them in a list
for i in range(int(Config.get('Auto', 'Last Line')), int(Config.get('Auto', 'Last Line')) + 500):
   if (i < len(book) - 1):
      if (len(book[i].strip())):
         text_lines  = text_lines + 1
      else:
         blank_lines = blank_lines + 1
         if text_lines >= int(Config.get('Book', 'Lines')):
            break

      audio_text.append(book[i])

# Update the config file with the line we stopped at
f = open(INI_FILE, 'w')
Config.set('Auto', 'Last Line', int(Config.get('Auto', 'Last Line')) + len(audio_text))
next_episode = int(Config.get('Youtube', 'Episode')) + 1
Config.set('Youtube', 'Episode', next_episode)
Config.write(f)

# Write the text to be converted out to a file
f = open('out.txt', 'w')
f.write('Episode number ' + str(next_episode) + '\n\n')
for line in audio_text:
   f.write(line.strip() + '\n')
f.close()

# Debug output
print 'Text Lines  : ' + str(text_lines)
print 'Blank Lines : ' + str(blank_lines)
print 'Total Length: ' + str(len(audio_text))

# Call the shell script that reads the text file generated above and runs it through espeak to create a WAV file
subprocess.call(['./make_audio.shl', Config.get('Auto', 'Speed'), Config.get('Auto', 'Voice')])

# Call the shell script that uses the book image and espeack WAV create above to generate an MP4 file
subprocess.call('./make_video.shl')

# Archive the video in case of errors uploading
if (not os.path.exists('videos/' + Config.get('Book', 'File').split('.')[0])):
   os.mkdir('videos/' + Config.get('Book', 'File').split('.')[0])

shutil.copy2('out.mp4', 'videos/' + Config.get('Book', 'File').split('.')[0] + '/' + str(next_episode) + '.mp4')

# Upload the file to Youtube and place it in a playlist
subprocess.call(['./upload.py', '--noauth_local_webserver', '--file', 'out.mp4'])
