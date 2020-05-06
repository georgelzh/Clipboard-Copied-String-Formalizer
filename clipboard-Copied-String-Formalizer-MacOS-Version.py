"""
!python3.7

clipboard-Copied-String-Formalizer.py
Author: Zhihong LI (zhihongli@bennington.edu)
Date: April 27, 2020

 - it formalize the string that user copies from the web, pdf or anywhere
else as long as it is string. Then it keeps the formalized string in the copy clipboard,
so that the user can just paste the formalized string without doing anything. 

The program will detect whether the user copied string or image, 
if its image, the program continur, if it's string, then it formalize it

"""

import clipboard
import time
from PIL import ImageGrab

print("Start formalizing str in clipboard...")

# initialization for the loop comparison use
copiedStr = "A1,2p;;[3[]0" # random string
while True:
	img = ImageGrab.grabclipboard()
	if type(img) != type(None):
		continue
	else:
		# if copied string changed, then formalize the str
		# and place it in the clipboard so that user can paste it. 
		copiedNewStr = clipboard.paste()
		if copiedNewStr != copiedStr:
			clipboard.copy(copiedNewStr)
			time.sleep(0.4)

"""
https://pypi.org/project/clipboard/
https://www.devdungeon.com/content/grab-image-clipboard-python-pillow
"""

