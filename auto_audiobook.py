#!/usr/bin/python2.7

BOOK_DIR  = 'books'
BOOK_FILE = 'tale_of_two_cities.txt'

f = open('last_line', 'r')
last_line = int(f.read())
f.close()

f = open(BOOK_DIR + '/' + BOOK_FILE, 'r')
book = f.read().split('\n')
f.close()

blank_lines = 0
text_lines  = 0
audio_text  = []
for i in range(last_line, last_line + 500):
   if (len(book[i].strip())):
      text_lines  = text_lines + 1
   else:
      blank_lines = blank_lines + 1
      if text_lines >= 50:
         break

   audio_text.append(book[i])

f = open('last_line', 'w')
f.write(str(last_line + i))
f.close()

f = open('out.txt', 'w')
for line in audio_text:
   f.write(line.strip() + '\n')
f.close()

f = open('number', 'r')
num = int(f.read())
f.close()

f = open('number', 'w')
f.write(str(num + 1))
f.close()

print 'Text Lines : ' + str(text_lines)
print 'Blank Lines: ' + str(blank_lines)
print audio_text
