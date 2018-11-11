from PyJdReader import PyJdReader

import os
from PIL import Image, ImageGrab



def main():
    reader = PyJdReader()
    fpr = "D:\jdReader\\"
    bn = "十万个小肉段"
    fp = fpr + bn + "\\"
    # fp = 'D:\jdReader\\aaaa\\'
    #screenshot
    # reader.savePage2Pictures(fp, 1, True)
    #save to pdf file
    pdfPath = fpr + bn + ".pdf"
    # reader.mergePictures2Pdf(fp, pdfPath)
    #convert images to black-white (or gray level) image
    reader.convert2Bw(fp, fp + "bw\\", False)
    pdf_path2 = fpr + bn + "bw.pdf"
    reader.mergePictures2Pdf(fp + "bw\\", pdf_path2)





if __name__ == '__main__':
    main()