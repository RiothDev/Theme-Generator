import os

fonts = {
    "1" : "Arial, Helvetica, sans-serif",
    "2" : "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
    "3" : "'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif",
    "4" : "Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif",
    "5" : "Georgia, 'Times New Roman', Times, serif"
}

properties = ["Image-Url", "Home-Url", "RGB-Color", "Main-Transparency", "Server-List-Width", "Main-Font-Size"]

def main():
    os.system("title Theme Generator")
    os.system("cls")

    print("- Code made by HazuDev (Credits to puckzxz for making the CSS template)\n")

    def createFile(content):
        with open("build/MyTheme.css", "w+") as mainFile:
            mainFile.write(content)
            mainFile.close()
        
        print('\n- The file was created in the "build" folder')
        input()

    def structure(config):
        with open("src/Template", "r") as readFile:
            content = readFile.read()

            for x in properties:
                content = content.replace(x, str(config[x]))

            try:
                content = content.replace("Main-Font", fonts[str(config["Main-Font"])])
            except:
                content = content.replace("Main-Font", config["Main-Font"])

            createFile(content)
            readFile.close()

    def askFor():
        backgroundUrl = str(input("> Background (URL) : "))
        homeUrl = str(input("> Home icon (URL) : "))
        font = str(input("> Font (1 - 5) : "))
        fontSize = str(input("> Font size (Default : 100%) : "))
        rgbColor = str(input("> Theme color (RGB) (Example : 24, 24, 24) : "))
        transparency = str(input("> Transparency (Default : 0.8) : "))
        serverList = str(input("> Server list width (Default : 65) : "))

        config = {
            "Image-Url" : backgroundUrl,
            "Home-Url" : homeUrl,
            "Main-Font" : font,
            "RGB-Color" : rgbColor,
            "Main-Transparency" : transparency,
            "Server-List-Width" : serverList,
            "Main-Font-Size" : fontSize
        }

        structure(config)
    
    askFor()

if __name__ == "__main__":
    main()
