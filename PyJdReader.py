import os

from PIL import Image, ImageGrab
from fpdf import FPDF
from pyJdHelper import PyJdHelper
from settings import Settings


def log(msg):
    print(msg)


class PyJdReader:
    def __init__(self, logger):
        self.settings = Settings()
        self.rect = self.settings.Rect
        self.helper = PyJdHelper()
        if logger is None:
            self.logger = self
        else:
            self.logger = logger


    def crop_image(self, rect):
        image = ImageGrab.grab()
        clip = image.crop(rect)
        return clip

    def pre_process(self, img):
        pass

    def has_more(self):
        self.helper.clickMouseLeft(self.settings.PercentBoxCenter)
        self.helper.pressCtrlAndKey('a')
        self.helper.pressCtrlAndKey('c')
        percent = self.helper.getClipboard()
        return float(percent) < 100

    def save2pictures(self, fp, startIndex = 1, fromStart = False):
        self.logger.write_line("hello. I am PyJdReader.")
        #1. Active the JdReader to foregroud
        self.helper.clickMouseLeft(self.settings.TaskBarLocation)
        if fromStart:
            #back to first page
            self.helper.clickMouseLeft(self.settings.FirstButtonCenter)

        # Screen Clipping
        pageNo = startIndex


        while self.has_more():
            img = self.crop_image(self.rect)
            fn = fp + '%05d' % pageNo + '.jpg'
            img.save(fn)
            self.logger.write_line('Save to ' + fn)
            pageNo += 1
            self.click_next_page()
        # The last page
        img = self.crop_image(self.rect)
        fn = fp + '%05d' % pageNo + '.jpg'
        img.save(fn)
        print('Save to ' + fn)
        return pageNo


    def click_next_page(self):
        self.helper.clickMouseLeft(self.settings.NextButtonCenter)

    def merge2pdf(self, imagesPath, pdfPath):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        for im in os.listdir(imagesPath):
            img = Image.open(imagesPath + im)
            pdf.add_page()
            pdf.image(imagesPath + im, -0, 0, pdf.w * 0.99, pdf.h * 0.99)  # , img.width, img.height)
        pdf.output(pdfPath, "F")

    def convert2grey(self, imagesPath, out_path, grey = False):
        page = 0
        for im in os.listdir(imagesPath):
            img = Image.open(imagesPath + im)
            page += 1
            if grey:
                img2 = img.convert('L')
            else:
                img2 = img.convert('1')
            if not os.path.exists(out_path):
                os.mkdir(out_path)
                log("mkdir " + out_path)
            img2.save(out_path + im)
        return page

    def write_line(self, msg):
        print(msg)
#         self.logger.write_line
