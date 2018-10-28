from PyJdReader import PyJdReader


def main(args):
    jdReader = PyJdReader()
    jdReader.run()
    # tmp = input("hello:")
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))