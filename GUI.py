import os, tkinter
from PIL import Image, ImageTk

assets = {
    "Icon" : [None, "src/Icon.png"]
}

fonts = {
    "1" : "Arial, Helvetica, sans-serif",
    "2" : "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
    "3" : "'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif",
    "4" : "Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif",
    "5" : "Georgia, 'Times New Roman', Times, serif"
}

properties = ["Image-Url", "Home-Url", "RGB-Color", "Main-Transparency", "Server-List-Width", "Main-Font-Size"]

def main():
    os.system("cls")

    root = tkinter.Tk()
    root.geometry("700x500")

    root.config(bg="#1a1a1a")

    def load_asset(a: str) -> ImageTk.PhotoImage:
        if a in assets:
            if assets[a][0] is None:
                try:
                    img = ImageTk.PhotoImage(Image.open(assets[a][1]))
                    assets[a][0] = img
                    return img
                except:
                    print("> Error trying to load asset {}".format(a))
                    return None
            else:
                return assets[a][0]
    
    for x in assets:
        load_asset(x)

    root.title("Theme Generator")
    root.iconphoto(True, assets["Icon"][0])

    frame = tkinter.Frame(master=root, bg="#242424")
    frame.pack(pady=30, padx = 30, fill="both", expand=True)

    label = tkinter.Label(master=frame, text="Theme Generator", font=("Lucida Sans Unicode", 20), fg="#f1f1f1", bg="#242424")
    label.pack(pady=12, padx=10)

    entry1 = tkinter.Entry(master=frame)
    entry1.insert(0, "Background (URL)")
    entry1.pack(pady=12, padx=10)

    entry2 = tkinter.Entry(master=frame)
    entry2.insert(0, "Home icon (URL)")
    entry2.pack(pady=12, padx=10)

    entry3 = tkinter.Entry(master=frame)
    entry3.insert(0, "Font (1 - 5)")
    entry3.pack(pady=12, padx=10)

    entry4 = tkinter.Entry(master=frame)
    entry4.insert(0, "Font size (Default : 100%)")
    entry4.pack(pady=12, padx=10)

    entry5 = tkinter.Entry(master=frame)
    entry5.insert(0, "Theme color (RGB) (Example : 24, 24, 24)")
    entry5.pack(pady=12, padx=10)

    entry6 = tkinter.Entry(master=frame)
    entry6.insert(0, "Transparency (Default : 0.8)")
    entry6.pack(pady=12, padx=10)

    entry7 = tkinter.Entry(master=frame)
    entry7.insert(0, "Server list width (Default : 65)")
    entry7.pack(pady=12, padx=10)

    def create_file(content: str):
        with open("build/MyTheme.css", "w+") as main_file:
            main_file.write(content)
            main_file.close()
    
    def proccess():
        config = {
            "Image-Url" : entry1.get(),
            "Home-Url" : entry2.get(),
            "Main-Font" : entry3.get(),
            "RGB-Color" : entry4.get(),
            "Main-Transparency" : entry5.get(),
            "Server-List-Width" : entry6.get(),
            "Main-Font-Size" : entry7.get()
        }

        with open("src/Template", "r") as read_file:
            content = read_file.read()

            for x in properties:
                content = content.replace(x, str(config[x]))

            try:
                content = content.replace("Main-Font", fonts[str(config["Main-Font"])])
            except:
                content = content.replace("Main-Font", config["Main-Font"])
            
            create_file(content=content)

            read_file.close()

    button = tkinter.Button(master=frame, text="Submit", command=proccess, bg="#556769", fg="#f1f1f1")
    button.pack(pady=12, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()