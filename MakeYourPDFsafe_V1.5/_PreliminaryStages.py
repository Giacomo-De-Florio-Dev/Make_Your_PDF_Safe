import _PreliminaryStages
import Config
import Platform_Detector
import PdfLock

from tkinter import messagebox

if Config.Check_Platform == True:
    if Platform_Detector.Current_Platform() in Config.Supported_Os:
        pass

    else:
        messagebox.showerror("Sorry, your system isn't supported yet", "{} isn't an OS supported by this program.".format(Platform_Detector.Current_Platform()))

else:
    pass
