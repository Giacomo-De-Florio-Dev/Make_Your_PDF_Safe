# MYPDFS - Make Your PDF Safe
## Program developed by Giacomo-De-Florio-Dev
This program will allow you to protect your PDF files with a password.
Every time someone tries to access the protected file, they will have to enter the password you set.

## What the program does and what it DOES NOT do.
- Sets a password to a copy, created when proceeding with security, of the PDF file
- Allows you to choose the PDF file and its destination through explorer (via tkinter.filedialog)
- All procedures are carried out through a fresh, elegant and clear graphical interface.
- Before proceeding with the protection of your PDF file, you will need to repeat the password 2 times.
- DOES NOT: Encrypt the PDF file directly.
- NOT: Use proprietary libraries to handle PDF. (1)
- DOES NOT: Remove the password from the protected file in any way. (2)

---
(1) : The program uses PyPDF2 to handle PDF files. The library is set up in the program, so no additional installation is required.

(2) : Just for the moment. I'm working on adding this feature.

## System requirements
- It is necessary to have Python 3 (Or Later) installed on the device.
- Available only for Windows (For the moment).

## Credits
- Images: [freepik, from user @storyset](https://www.freepik.com/stories)
- PDF management: [PyPDF2](https://pypi.org/project/PyPDF2/)
- Program Developed by [Giacomo-De-Florio-Dev](https://github.com/Giacomo-De-Florio-Dev/)

Program developed in Python.
