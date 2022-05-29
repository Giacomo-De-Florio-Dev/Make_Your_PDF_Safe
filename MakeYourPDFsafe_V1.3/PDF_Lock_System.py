import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def pdf_lock(basefile_path, dextin, password):
    basefile_path = basefile_path.replace("\\", "/")                          # Base file path
    basefile_name, basefile_extension = os.path.splitext(basefile_path)       # Base File name and extension
    cryptfile_path = os.path.dirname(os.path.realpath(basefile_path))         # crypt file path
    cryptfile_name = os.path.basename(basefile_path)                          # crypt file name
    cryptfile_name = os.path.splitext(cryptfile_name)[0]

    ## ## ## Create a copy of the base file. ## ## ##

    copy_system = ("copy " + basefile_path + " " + dextin+"\\"+cryptfile_name+"_protected"+basefile_extension)
    copy_system = copy_system.replace("/", "\\") # replace all "/" with a "\"

    print(copy_system)
    os.system(copy_system) # execute copy system.

    ## ## ## Crypting the copy of the BASE-FILE ## ## ##

    cryptfile_path_com = (dextin+"\\"+cryptfile_name+"_protected"+basefile_extension) # c:/users/username/path_to_the_folder_of_the_new_file + newfilename
    cryptfile_path_com.replace("/", "\\") # replace all "/" with "\"

    PDF_Write = PdfFileWriter()
    PDF_which_you_want_crypt = PdfFileReader(cryptfile_path_com)

    for pagenum in range(PDF_which_you_want_crypt.numPages):
        PDF_Write.addPage(PDF_which_you_want_crypt.getPage(pagenum))

    PDF_Write.encrypt(password)

    with open(cryptfile_path_com, "wb") as f:
        PDF_Write.write(f)
        f.close()

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

if __name__ == "__main__":
    print("########################################################################################")
    path_to_the_file = input("Path to the file: ")
    print("########################################################################################")
    path_to_the_final_file = input("Insert the dextination of you encrypted PDF file: ")
    print("########################################################################################")
    print("")

    while True:
        password = input("Password: ")
        password_retype = input("Re-type Password: ")

        if password == password_retype:
            break

        else:
            print("########################################################################################")
            print("Passwords does not match. Try again.")
            print("########################################################################################")
            print("")
            continue

    path_to_the_final_file = path_to_the_final_file.replace('"', '')
    path_to_the_file = path_to_the_file.replace('"', '')

    print(path_to_the_final_file)

    pdf_lock(path_to_the_file, path_to_the_final_file, password)