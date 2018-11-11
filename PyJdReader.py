import os

from PIL import Image, ImageGrab
from fpdf import FPDF
from pyJdHelper import PyJdHelper
from settings import Settings


def log(msg):
    print(msg)


class PyJdReader:
    def __init__(self):
        self.settings = Settings()
        self.rect = self.settings.Rect
        self.helper = PyJdHelper()


    def clipImage(self, rect):
        image = ImageGrab.grab()
        clip = image.crop(rect)
        return clip

    def preProcess(self, img):
        pass

    def hasMore(self):
        self.helper.clickMouseLeft(self.settings.PercentBoxCenter)
        self.helper.pressCtrlAndKey('a')
        self.helper.pressCtrlAndKey('c')
        percent = self.helper.getClipboard()
        return float(percent) < 100

    def savePage2Pictures(self, fp, startIndex = 1, fromStart = False):
        print("hello. I am PyJdReader.")
        #1. Active the JdReader to foregroud
        self.helper.clickMouseLeft(self.settings.TaskBarLocation)
        if fromStart:
            #back to first page
            self.helper.clickMouseLeft(self.settings.FirstButtonCenter)

        # Screen Clipping
        pageNo = startIndex


        while self.hasMore():
            img = self.clipImage(self.rect)
            fn = fp + '%05d' % pageNo + '.jpg'
            img.save(fn)
            print('Save to ' + fn)
            pageNo += 1
            self.clickNextPage()
        # The last page
        img = self.clipImage(self.rect)
        fn = fp + '%05d' % pageNo + '.jpg'
        img.save(fn)
        print('Save to ' + fn)
        pageNo += 1

    def clickNextPage(self):
        self.helper.clickMouseLeft(self.settings.NextButtonCenter)

    def mergePictures2Pdf(self, imagesPath, pdfPath):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        for im in os.listdir(imagesPath):
            img = Image.open(imagesPath + im)
            pdf.add_page()
            pdf.image(imagesPath + im, -0, 0, pdf.w * 0.99, pdf.h * 0.99)  # , img.width, img.height)
        pdf.output(pdfPath, "F")

    def convert2Bw(self, imagesPath, out_path, gray = False):
        for im in os.listdir(imagesPath):
            img = Image.open(imagesPath + im)
            if gray:
                img2 = img.convert('L')
            else:
                img2 = img.convert('1')
            if not os.path.exists(out_path):
                os.mkdir(out_path)
                log("mkdir " + out_path)
            img2.save(out_path + im)

