from PIL import Image
from PIL import ImageGrab
import pytesseract

im = ImageGrab.grab()
im.show()

print "input anything to end program"
raw_input()