import config_file
import platform_detector
from tkinter import messagebox

def platCheck():
    if config_file.check_the_platform[0] == "Y":
        if config_file.check_the_platform[1] == platform_detector.detect_plataform():
            return "PLAT:OK"
        
        else:
            messagebox.showerror("Your system isn't supported yet...", "Your system isn't supported yet. If you think it's a mistake, go to the program folder and modify the config_file.py. By default the program run on Microsoft® Windows.")
            return "PLAT:ERROR"

    elif config_file.check_the_platform[0] == "N":
        return "PLAT:OK"

    else:
        messagebox.showwarning("Something went wrong", "Sorry, something went wrong > ErrorCode:osPlatform:configFile:check_the_platform[0]")
        return "PLAT:ERROR"