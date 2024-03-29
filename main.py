import tkinter as tk
import tkinter.font as tkFont
from tkinter import RAISED, NW

from PIL import ImageTk, Image


class App:
    def __init__(self, root):
        # setting title
        root.title("Car Driving Analyzer")
        # setting window size
        width = 263
        height = 403
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_312 = tk.Button(root)
        GButton_312["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_312["font"] = ft
        GButton_312["fg"] = "#000000"
        GButton_312["justify"] = "center"
        GButton_312["text"] = "Analyze"
        GButton_312.place(x=70, y=280, width=91, height=30)
        GButton_312["command"] = self.GButton_312_command

        GLineEdit_203 = tk.Entry(root)
        GLineEdit_203["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_203["font"] = ft
        GLineEdit_203["fg"] = "#333333"
        GLineEdit_203["justify"] = "center"
        GLineEdit_203["text"] = "Entry"
        GLineEdit_203.place(x=10, y=150, width=223, height=30)

        GLabel_501 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_501["font"] = ft
        GLabel_501["fg"] = "#333333"
        GLabel_501["justify"] = "center"
        GLabel_501["text"] = "Snow precipitation (mm)"
        GLabel_501.place(x=10, y=110, width=144, height=30)

        GLabel_27 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_27["font"] = ft
        GLabel_27["fg"] = "#333333"
        GLabel_27["justify"] = "center"
        GLabel_27["text"] = "Wind speed (km/h)"
        GLabel_27.place(x=10, y=190, width=114, height=30)

        GLabel_734 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_734["font"] = ft
        GLabel_734["fg"] = "#333333"
        GLabel_734["justify"] = "center"
        GLabel_734["text"] = "Car driving risk:"
        GLabel_734.place(x=10, y=330, width=109, height=30)

        GLineEdit_826 = tk.Entry(root)
        GLineEdit_826["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_826["font"] = ft
        GLineEdit_826["fg"] = "#333333"
        GLineEdit_826["justify"] = "center"
        GLineEdit_826["text"] = "Entry2"
        GLineEdit_826.place(x=10, y=230, width=221, height=30)

        GMessage_480 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_480["font"] = ft
        GMessage_480["fg"] = "#333333"
        GMessage_480["justify"] = "center"
        GMessage_480["text"] = "Message"
        GMessage_480.place(x=120, y=330, width=80, height=25)

        # Create an object of tkinter ImageTk
        original_image = Image.open("car-weather.png")
        img_resize = original_image.resize((100, 100))
        img = ImageTk.PhotoImage(img_resize)
        # Create a Label Widget to display the text or Image
        label = tk.Label(root, image = img)
        label.pack()
        label.place(x=80, y=10, width=100, height=100)
        root.mainloop()

    def GButton_312_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
