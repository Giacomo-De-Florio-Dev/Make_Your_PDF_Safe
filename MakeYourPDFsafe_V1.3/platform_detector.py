from sys import platform

def detect_plataform():

    if platform == "linux" or platform == "linux2":
        return "PLATFORM:OS:LINUX"

    elif platform == "darwin":
        return "PLATFORM:OS:MACOS"
    
    elif platform == "win32":
        return "PLATFORM:OS:WIN"
    
if __name__=="__main__":
    detect_plataform()