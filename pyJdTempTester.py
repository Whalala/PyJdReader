from PyJdReader import PyJdReader

import os
from PIL import Image, ImageGrab


def test_run_reader():
    reader = PyJdReader()
    fpr = "D:\jdReader\\"
    bn = "十万个小肉段"
    fp = fpr + bn + "\\"
    # fp = 'D:\jdReader\\aaaa\\'
    # screenshot
    # reader.savePage2Pictures(fp, 1, True)
    # save to pdf file
    pdfPath = fpr + bn + ".pdf"
    # reader.mergePictures2Pdf(fp, pdfPath)
    # convert images to black-white (or gray level) image
    reader.convert2grey(fp, fp + "bw\\", False)
    pdf_path2 = fpr + bn + "bw.pdf"
    reader.merge2pdf(fp + "bw\\", pdf_path2)


def test_picture_format():
    path = "d:\jdReader\\"
    im = Image.open(path + "00002.jpg")
    img = im.convert('L')
    imb = im.convert('1')
    im.save(path + "00001.png")
    img.save(path + "gr.jpg")
    img.save(path + "gr.png")
    imb.save(path + "bw.jpg")
    imb.save(path + "bw.png")
    


def main():
    # test_run_reader()
    test_picture_format()





if __name__ == '__main__':
    main()