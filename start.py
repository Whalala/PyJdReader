from PyJdReader import PyJdReader

class Logger:
    def __int__(self):
        pass

    def write_line(self, msg):
        print(">>>>>>")
        print(msg)

def main():
    lg = Logger()
    reader = PyJdReader(lg)
    fpr = "D:\jdReader\\"
    bn = "郑渊洁四大名传"
    fp = fpr + bn + "\\"

    # screenshot
    count = reader.save2pictures(fp, 1, True)
    lg.write_line("Save all to images[%d pages]." % count)

    # save to pdf file (colorful)
    pdfPath = fpr + "pdf\\" + bn + ".pdf"
    reader.merge2pdf(fp, pdfPath)
    lg.write_line("Saved to " + pdfPath)

    # convert images to grey level image
    greyPath = fpr + "grey\\" + bn + "\\"
    lg.write_line("Converting all pictures to grey level images...")
    pages = reader.convert2grey(fp, greyPath, True)
    lg.write_line("[%d] images converted." % pages)


    pdf_path2 = fpr+"pdf\\" + bn + "grey.pdf"
    lg.write_line("Merging images into pdf file...")
    reader.merge2pdf(greyPath, pdf_path2)
    lg.write_line("Saved to " + pdf_path2)

    lg.write_line("All done.")
    return 0








if __name__ == '__main__':
    main()