import pytesseract

import PIL.Image

import cv2


"""
Page Segmentation modes:

#These are basicallly the configs that  I an gonna use to extract different sort of texts from image or video files.

  0    Orientatation and script detection (OSD) only.

  1    Automatic Page segmentation with OSD.

  2    Automatic Page Segmentation, but no OSD, or OCR.

  3    Fully automatic page segmentation, but no OSD (Default)

  4    Assume a single column of text of variable sizes.

  5    Assume a single a uniform block of vertically aligned text.

  6    Assume a single uniform block of text.

  7    Treat the image as single text line.

  8    Treat the image as single word.

  9    Treat the image as single word in a circle.

 10    Treat the image as single character.

 11    Sparse text. Find as much text as possibble in no perticular order.
 
 12    Sparse text with OSD.

 13    Raw line. Treat the image as a sinle text line,
                       bypassing hacks that are Tesseract-specific.
"""

"""
OCR Engine Mode

0    Legacy engine only.

1    Neural Nets LSTM engine only.

2    Legacy + LSTM engines.

3    Default, based on what is available.
"""

myconfig = r"--psm 6 --oem 3"
# psm6 and oem3 basically denotes the use of 6th and 3rd modes of config from above two  modes respectively.

text = pytesseract.image_to_string(PIL.Image.open("testfile.jpg"), config=myconfig)


print(text)