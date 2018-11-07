from PIL import Image, ImageGrab

from pyJdHelper import PyJdHelper
from settings import Settings





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

    def savePage2Pictures(self, fp, fromStart = False):
        print("hello. I am PyJdReader.")
        #1. Active the JdReader to foregroud
        self.helper.clickMouseLeft(self.settings.TaskBarLocation)
        if fromStart:
            #back to first page
            self.helper.clickMouseLeft(self.settings.FirstButtonCenter)

        # Screen Clipping
        pageNo = 1
        while self.hasMore():
            img = self.clipImage(self.rect)
            fn = fp + '%05d' % pageNo + '.png'
            img.save(fn)
            print('Save to ' + fn)
            pageNo += 1
            self.clickNextPage()

    def clickNextPage(self):
        self.helper.clickMouseLeft(self.settings.NextButtonCenter)
