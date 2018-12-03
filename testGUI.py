import tkinter



def main():
    root = tkinter.Tk()
    root.title = "ReaderCapture"
    root.geometry("800x600")
    label = tkinter.Label(root, text='I am JdReader Capturer.')
    # label.pack()
    mf = root
    # mf = tkinter.Frame(root, width=800, height=500, bg="#00FF00")

    lf = tkinter.Frame(mf, bg="#d3d3d3")
    lf['width'] = 200
    lf["height"] = 500
    lbl = tkinter.Label(lf, text="Click button to get the locations:")
    lblpos = tkinter.Label(lf,)
    btnfirstpage = tkinter.Button(lf, text="Get first page button")
    lbl.pack(side=tkinter.TOP)
    btnfirstpage.pack(side=tkinter.TOP)
    # lf.pack(side=tkinter.LEFT)
    lf.grid(row = 0, column = 0)

    imgpath = "D:\\jdReader\\rbg.jpg"
    rf = tkinter.Frame(mf)
    cvs = tkinter.Canvas(rf)
    # img = tkinter.Image(master=rf, name=imgpath)


    # cvs.image_names(imgpath)
    # tkinter.Image("D:\\jdReader\\rbg.jpg")
    # rf.pack(side=tkinter.RIGHT)
    rf.grid(row = 0, column = 1)

    # mf.pack()
    tkinter.mainloop()


if __name__ == '__main__':
    main()