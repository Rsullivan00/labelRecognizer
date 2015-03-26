import cv2
import os
from subprocess import Popen, PIPE, call

# No luck with pytesseract or python3-tesseract
def apply_tesseract(im_path):
    temp_file = "temp"
    p = Popen(["tesseract", im_path, temp_file], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    temp_file += ".txt"
    output = open(temp_file).read()
#    os.remove(temp_file)
#    print("OCR output:\n%s" % output)

    return output