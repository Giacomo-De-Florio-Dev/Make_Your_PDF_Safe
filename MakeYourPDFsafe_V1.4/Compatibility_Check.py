import Config_File
import Platform_Detector
from tkinter import messagebox

def Os_Compatibility():
    if Config_File.check_the_platform[0] == "Y":
        if Config_File.check_the_platform[1] == Platform_Detector.detect_plataform():
            return True
        
        else:
            messagebox.showerror("Your system isn't supported yet...", "Your system isn't supported yet. If you think it's a mistake, go to the program folder and modify the config_file.py. By default the program run on Microsoft® Windows.")
            return False

    elif Config_File.check_the_platform[0] == "N":
        return True

    else:
        messagebox.showwarning("Something went wrong", "Sorry, something went wrong > ErrorCode:osPlatform:configFile:check_the_platform[0]")
        return False