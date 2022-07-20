from sys import platform

def Current_Platform():

    if platform == "linux" or platform == "linux2":
        return "Linux"

    elif platform == "darwin":
        return "Mac Os"
    
    elif platform == "win32":
        return "Windows"
    
if __name__=="__main__":
    Current_Platform()