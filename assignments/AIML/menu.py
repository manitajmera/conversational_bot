import os
import sys
from PIL import Image
def open_photo(menu):
    img=Image.open(menu)
    img.show()
if len(sys.argv)<=2:
    open_photo(sys.argv[1]+".jpg")
    print(len(sys.argv))
else:
    print(sys.argv)
    open_photo(sys.argv[1]+" "+sys.argv[2]+".jpg")

#print(len(sys.argv))

#print(sys.argv)
#open_photo("wazwan"+".jpg")
