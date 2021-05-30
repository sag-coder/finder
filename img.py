import urllib.request
from tkinter import *

from PIL import Image
url = 'https://techcrunch.com/wp-content/uploads/2020/06/GettyImages-1193112376.jpg?w=600'
image = Image.open(urllib.request.urlopen(url))
width, height = image.size
print (width,height)

root=TK()

root.mainloop()