#!/usr/bin/python3

import sys
import re
import os

with open('desc.txt', 'r') as f:
    while 1:
        line = f.readline()
        if line == '': # EOF
            break
        sys.stdout.write(line)
        if re.match('^\s$', line, re.UNICODE): # skip empty lines
            continue
        line2 = f.readline()
        m = re.match('^\s*(.+?)\.\s*(.+)$', line)
        assert(m)
        fn = m.group(1)
        desc1 = m.group(2)
        assert(fn)
        assert(desc1)
        desc = desc1.strip() + ' ' + line2.strip()

        # http://www.imagemagick.org/Usage/annotating/#annotating
        cmd = "width=`identify -format %w '{}'`; convert -resize 40% -background '#0008' -fill white -gravity center -size ${{width}}x100 caption:'{}' '{}' +swap -gravity south -composite '{}'".format(fn+'.jpg', desc, fn + '.jpg', fn + 'cap.jpg')
        print(cmd)
        r = os.system(cmd) 
        print('<', r, '>', fn, ' / ', desc)
        

