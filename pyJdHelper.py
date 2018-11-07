import time
import pyperclip as ppc
import pyautogui as pag

class PyJdHelper:
    def __int__(self):
        pass

    def getMousePoint(self):
        return pag.position()

    def clickMouseLeft(self, p):
        pag.click(p[0], p[1])

    def pressCtrlAndKey(self, key):
        pag.hotkey('ctrl', key)

    def getClipboard(self):
        return ppc.paste()


def printMousePoint():
    helper = PyJdHelper()
    while True:
        x, y = helper.getMousePoint()
        print(x, y)
        time.sleep(0.1)


def testPercent():
    printMousePoint()
    helper = PyJdHelper()
    helper.clickMouseLeft(1317, 1055)
    hasNext = True
    while hasNext:
        helper.clickMouseLeft(786, 57)
        helper.clickMouseLeft(714, 68)
        helper.pressCtrlAndKey('a')
        helper.pressCtrlAndKey('c')
        percent = helper.getClipboard()
        print (percent)
        hasNext = float(percent) < 100

def main():
    printMousePoint()

if __name__ == '__main__':
    main()