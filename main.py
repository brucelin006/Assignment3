"""
Authors: Gia Ky Huynh, Gaici Lin
"""
import tkinter as tk
import tkinter.font as tkFont
import fuzzylogic as fuzzy
from PIL import ImageTk, Image


class App:
    def __init__(self, root):
        # setting title and config window size
        root.title("Car Driving Analyzer")
        width = 263
        height = 420
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Create image
        original_image = Image.open("car-weather.png")
        img_resize = original_image.resize((100, 100))
        img = ImageTk.PhotoImage(img_resize)
        # Create a Label Widget to display the text or Image
        label = tk.Label(root, image=img)
        label.pack()
        label.place(x=80, y=10, width=100, height=100)

        # Create Snow precipitation label
        snow_prec_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        snow_prec_label["font"] = ft
        snow_prec_label["fg"] = "#333333"
        snow_prec_label["justify"] = "center"
        snow_prec_label["text"] = "Snow precipitation (mm)"
        snow_prec_label.place(x=10, y=110, width=160, height=30)

        # Create Snow Precipitation entry
        self.snow_prec_entry = tk.Entry(root)
        snow_prec_entry = self.snow_prec_entry
        snow_prec_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=15)
        snow_prec_entry["font"] = ft
        snow_prec_entry["fg"] = "#333333"
        snow_prec_entry["justify"] = "center"
        snow_prec_entry["text"] = "Snow Entry"
        snow_prec_entry.place(x=10, y=150, width=223, height=30)

        # Create Wind Speed label
        wind_speed_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        wind_speed_label["font"] = ft
        wind_speed_label["fg"] = "#333333"
        wind_speed_label["justify"] = "center"
        wind_speed_label["text"] = "Wind speed (km/h)"
        wind_speed_label.place(x=10, y=190, width=130, height=30)

        # Create Wind Speed entry
        self.wind_speed_entry = tk.Entry(root)
        wind_speed_entry = self.wind_speed_entry
        wind_speed_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=15)
        wind_speed_entry["font"] = ft
        wind_speed_entry["fg"] = "#333333"
        wind_speed_entry["justify"] = "center"
        wind_speed_entry["text"] = "Entry2"
        wind_speed_entry.place(x=10, y=230, width=221, height=30)

        # Create Analyze button
        analyzer_btn = tk.Button(root)
        analyzer_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=15)
        analyzer_btn["font"] = ft
        analyzer_btn["fg"] = "#000000"
        analyzer_btn["justify"] = "center"
        analyzer_btn["text"] = "Analyze"
        analyzer_btn.place(x=70, y=280, width=91, height=30)
        analyzer_btn["command"] = self.analyze_weather

        # Create Driving Risk Label
        driving_risk_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        driving_risk_label["font"] = ft
        driving_risk_label["fg"] = "#333333"
        driving_risk_label["justify"] = "center"
        driving_risk_label["text"] = "Car driving risk:"
        driving_risk_label.place(x=10, y=330, width=109, height=30)

        # Create Driving Risk value
        self.risk_level_msg = tk.Message(root, width=100)
        risk_level_msg = self.risk_level_msg
        ft = tkFont.Font(family='Times', size=15, weight=tkFont.BOLD)
        risk_level_msg["font"] = ft
        risk_level_msg["fg"] = "#333333"
        risk_level_msg["justify"] = "left"
        risk_level_msg["text"] = ""
        risk_level_msg.place(x=115, y=323, width=112, height=43)

        self.error_msg = tk.Message(root, fg="red", width=200)
        error_msg = self.error_msg
        error_msg["text"] = ""
        error_msg["font"] = tkFont.Font(family='Times', size=13)
        error_msg.place(x=10, y=355, width=250, height=50)

        root.mainloop()

    # method to integrate with fuzzy logic
    def analyze_weather(self):
        try:
            snow_precipitation = int(self.snow_prec_entry.get())
            wind_speed = int(self.wind_speed_entry.get())
            risk = fuzzy.get_fuzzy_output(wind_speed, snow_precipitation)
            self.risk_level_msg.config(text=str(risk))
            self.error_msg.config(text="")
        except Exception as e:
            error_message = str(e)
            if "invalid literal" in error_message:
                error_message = "Snow precipitation and Wind speed only allow number"
            # Display the error message
            self.error_msg.config(text=error_message)
            self.risk_level_msg.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
