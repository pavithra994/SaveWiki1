from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, X, StringVar
from tkinter.ttk import Frame, Button, Style, Label, Entry

from controller import WikipediaController, GoogleDriveController

IMAGE_LIST = [
    {
        "name": "wallpaper.jpg",
        "resolution": "300x450",
        "size": "450kb"
    },
    {
        "name": "wallpaper1.jpg",
        "resolution": "300x450",
        "size":"450kb"
    },
{
        "name": "wallpaper2.jpg",
        "resolution": "300x450",
        "size":"450kb"
    },
]


class MainWindowFrame(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.title("Save Wikipedia")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        title_l = Label(frame,text="Enter your Wikipedia URL")
        title_l.pack(fill=X)
        self.url_string = StringVar()

        url_entity = Entry(frame,textvariable=self.url_string)
        url_entity.pack(fill=X)


        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="submit",command=self.submit)
        okButton.pack(side=RIGHT)

    def submit(self):
        print("submit... " + self.url_string.get())
        try:
            wiki = WikipediaController(self.url_string.get())
        except:
            pass #TODO:

        temp_file = wiki.download_pdf()

        google = GoogleDriveController()
        google.upload(**temp_file)


def main():

    root = Tk()
    root.geometry("300x100+300+300")
    app = MainWindowFrame()
    root.mainloop()


if __name__ == '__main__':
    main()