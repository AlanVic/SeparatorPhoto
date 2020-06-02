import os
import cv2

pathOrigin = '/Users/alanvictor/Desktop/FotosInstaIBNA'


files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(pathOrigin):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)