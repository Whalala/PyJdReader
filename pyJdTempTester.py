from PyJdReader import PyJdReader


def main():
    reader = PyJdReader()
    fp = "D:\jdReader\\a\\"
    fp = 'D:\jdReader\借我执拗如少年\\'
    reader.savePage2Pictures(fp, True)


if __name__ == '__main__':
    main()