import subprocess
import os

from sys import platform

pypdf2_Unavaible = 0

def copyCommandbyPlatform():

    if platform == "linux" or platform == "linux2":
        return "cp "

    elif platform == "darwin":
        return "cp "
    
    elif platform == "win32":
        return "copy "

def InstallPyPDF2():
    subprocess.call(['pip', 'install', 'pypdf2'])
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter, errors

except ModuleNotFoundError:

    pypdf2_Unavaible = 1

    print("Sorry, this program need PyPDF2 to run.")
    while True:
        install_pypdf2 = input("Do you want to install PyPDF2? [Y/y - N/n] [Y]: ")
        if install_pypdf2 == "y" or InstallPyPDF2 == "Y":
            pypdf2_Unavaible = 0
            InstallPyPDF2()
            break
        elif install_pypdf2 == "n" or InstallPyPDF2 == "N":
           break
        elif install_pypdf2 == "":
            pypdf2_Unavaible = 0
            InstallPyPDF2()
            break
        else:
            print("Please, use only Y (or y) for Yes, N (or n) for No.")
            continue
    
    if install_pypdf2 == "n" or install_pypdf2 == "N" and pypdf2_Unavaible == 1:
        print("Quit.")
        quit()

def protect(baseFilePath, protectedFilePassword, protectedFileFolderDestination = "Default"):

    protectedFileFolderDestination = protectedFileFolderDestination.replace("\"", "")

    baseFileExtension = os.path.splitext(baseFilePath)[1]
    baseFileName = os.path.splitext(os.path.basename(baseFilePath))[0]

    if baseFileExtension.replace("\"", "") == ".pdf":
        print("Selected PDF file {}".format(baseFilePath))

    else:
        print("Sorry, but the file {} isn't a PDF file.".format(baseFilePath))
        exit()

    if protectedFileFolderDestination == "Default":
        destinationPath = baseFilePath.replace("'", "")
        destinationPath = destinationPath.replace("\"", "")

        destinationPath = destinationPath.replace("/", "\\")

    else:
        departurePath = baseFilePath

        protectedFileFolderDestination.replace("\"", "")
        protectedFileFolderDestination.replace("'", "")

        if protectedFileFolderDestination.endswith("\\") or protectedFileFolderDestination.endswith("/"):
            destinationPath = protectedFileFolderDestination+baseFileName+"_protected"+baseFileExtension

        else:
            destinationPath = protectedFileFolderDestination+"\\"+baseFileName+"_protected"+baseFileExtension

        destinationPath = destinationPath.replace("\"", "")
        destinationPath = destinationPath.replace("'", "")

        destinationPath = "\""+destinationPath+"\""

        cp = copyCommandbyPlatform()
        copy_command = (cp + departurePath + " " + destinationPath)
        copy_command = copy_command.replace("/", "\\")

        os.system(copy_command)

        destinationPath = destinationPath.replace("\"", "")
        destinationPath = destinationPath.replace("'", "")

    try:
        PDF_File_Writer = PdfFileWriter()
        PDF_File_Target = PdfFileReader(destinationPath)

        for numPages in range(PDF_File_Target.numPages):
            PDF_File_Writer.addPage(PDF_File_Target.getPage(numPages))

        PDF_File_Writer.encrypt(protectedFilePassword)

        with open(destinationPath, "wb") as file:
            PDF_File_Writer.write(file)
            file.close()

        if protectedFileFolderDestination == 0: 
            print("Your PDF file ({}) was successfully Protected with your password.".format(baseFilePath))

        else:
            print("Your PDF file ({}) was successfully Protected in ({}) with your password.".format(baseFilePath, destinationPath, protectedFilePassword))

    except errors.PdfReadError as e:
        print(e)
