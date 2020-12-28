#!/usr/bin/env python3

import sys
import os
from PIL import Image
new_dir = sys.argv[2]
try:
    directory = sys.argv[1]
    print('Processing images in ' + directory)
    for root ,dirs ,files in os.walk(directory,topdown=False):
        for name in files:
            path = os.path.join(root,name)
            try:
                im = Image.open(path)
                if im.format == 'TIFF':
                    img=im.convert('RGB').rotate(90).resize((128,128))
                    new_path=os.path.join(new_dir,name)
                    print(new_path)
                    img.save(new_path,'JPEG')
            except Exception as e:
                print(e)

except Exception as e:
    print(e)
