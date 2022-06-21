import Compatibility_Check

if Compatibility_Check.Os_Compatibility():
    import Mainpage_Launcher
    Mainpage_Launcher.Mainpage()

else:
    print(">>> Compatibility Check: Failed.")
    pass

quit()