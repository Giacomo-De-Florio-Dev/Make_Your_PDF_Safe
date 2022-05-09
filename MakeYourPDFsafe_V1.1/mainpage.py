from email.policy import default
from glob import glob
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pdf_lock_system
import os

def mainpage():
    fileopenfilter = dict(defaultextension=".pdf", filetypes=[("Select a PDF file.", ".pdf")], initialdir="C:/Users/{}/".format(os.getlogin()), title="Select a PDF file to crypt.")
    main_path = os.path.dirname(os.path.abspath(__file__))
    
    mpage = Tk()
    mpage.geometry("925x500+300+100")
    mpage.title("MYPDFS - Make Your PDF Safe")
    mpage.config(background="white")
    mpage.resizable(False, False)
    
    Protected_File_Image = PhotoImage(file=main_path+"\\imgs\\mainp_img.png")
    Label(mpage, image=Protected_File_Image, border=0).place(x=10, y=40)
    
    head_frame = Frame(mpage, width=450, height=480, background="white")
    head_frame.place(x=464, y=10)
    
    head_title = Label(head_frame, width=30, background="white", text="Make Your PDF Safe", fg="#00dfc0",font=("Microsoft YaHei light", "15", "bold"))
    head_title.place(x=10, y=10)
    
    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    
    def on_enter_PDFPATH(x):
        pdf_path = pdf_file_path_label.get()
        if pdf_path == "Insert the path of your PDF file":
            pdf_file_path_label.delete(0, END)
    
    def on_leave_PDFPATH(x):
        pdf_path = pdf_file_path_label.get()
        if pdf_path == "":
            pdf_file_path_label.insert(0, "Insert the path of your PDF file")
    
    ### ### ###
    
    def on_enter_ENPDFPATH(x):
        en_pdf_path = en_pdf_file_path_label.get()
        if en_pdf_path == "Enter the destination of the secured PDF":
            en_pdf_file_path_label.delete(0, END)
    
    def on_leave_ENPDFPATH(x):
        en_pdf_path = en_pdf_file_path_label.get()
        if en_pdf_path == "":
            en_pdf_file_path_label.insert(0, "Enter the destination of the secured PDF")
    
    ### ### ###
    
    def on_enter_PWD(x):
        passwd = en_pdf_file_password.get()
        if passwd == "Enter the password you use to unlock the PDF here":
            en_pdf_file_password.delete(0, END)
            en_pdf_file_password.config(show="*")
    
    def on_leave_PWD(x):
        passwd = en_pdf_file_password.get()
        if passwd == "":
            en_pdf_file_password.insert(0, "Enter the password you use to unlock the PDF here")
            en_pdf_file_password.config(show="")
        elif passwd != "Enter the password you use to unlock the PDF here":
            en_pdf_file_password.config(show="*")
    
    ### ### ###
    
    def show_password():
        if en_pdf_file_password.cget("show") == "*" and en_pdf_file_password.get() != "Enter the password you use to unlock the PDF here":
            en_pdf_file_password.config(show="")
        elif en_pdf_file_password.cget("show") == "" and en_pdf_file_password.get() != "Enter the password you use to unlock the PDF here":
            en_pdf_file_password.config(show="*")

    ### #

    def on_enter_REPASS(x):
        repasswd = retype_passwd.get()
        if repasswd == "Re-type the password":
            retype_passwd.delete(0, END)
            retype_passwd.config(show="*")
    
    def on_leave_REPASS(x):
        repasswd = retype_passwd.get()
        if repasswd == "":
            retype_passwd.insert(0, "Re-type the password")
            retype_passwd.config(show="")

    ### ### ### ###
    
    def Browse_PDF():
        pdffilepath = filedialog.askopenfilename(**fileopenfilter)

        if pdffilepath != "":
            pdf_file_path_label.delete(0, END)
            pdf_file_path_label.insert(0, pdffilepath.replace("/", "\\"))
        
            en_pdf_file_prevdex = os.path.dirname(os.path.realpath(pdffilepath))
            en_pdf_file_path_label.delete(0, END)
            en_pdf_file_path_label.insert(0, en_pdf_file_prevdex)
    
    
    def Browse_Dir():
        enpdffiledex = filedialog.askdirectory()

        if enpdffiledex != "":
            en_pdf_file_path_label.delete(0, END)
            en_pdf_file_path_label.insert(0, enpdffiledex.replace("/", "\\"))
    
    ### ### ### ### ###
    
    def Crypt_The_Pdf():
        global pdf_path, encrypt_pdf_path, password
    
        pdf_path = pdf_file_path_label.get()
        encrypt_pdf_path = en_pdf_file_path_label.get()
        password = en_pdf_file_password.get()
        repass = retype_passwd.get()

        if pdf_path != "Insert the path of your PDF file" and pdf_path != "" and pdf_path != " ":
            if encrypt_pdf_path != "Enter the destination of the secured PDF" and encrypt_pdf_path != "" and encrypt_pdf_path != " ":
                if password != "Enter the password you use to unlock the PDF here" and password != "" and password != " ":
                    if password == repass:
                        pdf_path = pdf_path.replace("/", "\\")
                        encrypt_pdf_path = encrypt_pdf_path.replace("/", "\\")
                    
                        pdf_lock_system.pdf_lock(pdf_path, encrypt_pdf_path, password)
                    
                        messagebox.showinfo("Mission accomplished", "The PDF is now protected with a password")
                    
                        pdf_file_path_label.delete(0, END)
                        en_pdf_file_path_label.delete(0, END)
                        en_pdf_file_password.delete(0, END)
                    
                        pdf_file_path_label.insert(0, "Insert the path of your PDF file")
                        en_pdf_file_path_label.insert(0, "Enter the destination of the secured PDF")
                        en_pdf_file_password.insert(0, "Enter the password you use to unlock the PDF here")
                        en_pdf_file_password.config(show="")
                        retype_passwd.config(show="")
                        retype_passwd.delete(0, END)
                        retype_passwd.insert(0, "Re-type the password")
                    else:
                        messagebox.showerror("Something went wrong", "Password doesn't match!")
                else:
                    messagebox.showerror("Something went Wrong", "Please, fill in all fields.")
            else:
                messagebox.showerror("Something went Wrong", "Please, fill in all fields.")
        else:
            messagebox.showerror("Something went Wrong", "Please, fill in all fields.")
    
    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    
    ## ## ## PDF file path ## ## ##
    
    pdf_file_path_label = Entry(head_frame, width=45, border=0,font=("Microsoft YaHei light", "10", "bold"))
    pdf_file_path_label.place(x=10, y=60)
    pdf_file_path_label.insert(0, "Insert the path of your PDF file")
    pdf_file_path_label.bind("<FocusIn>", on_enter_PDFPATH)
    pdf_file_path_label.bind("<FocusOut>", on_leave_PDFPATH)
    
    pdf_file_path_label_cursor_frame = Frame(head_frame, width=355, height=1.4, background="black")
    pdf_file_path_label_cursor_frame.place(x=10, y=85)
    
    pdf_file_path_browse_label = Label(head_frame, width=40, background="white", text="Don't you want to manually enter the path?")
    pdf_file_path_browse_label.place(x=10, y=90)
    
    pdf_file_path_browse_button = Button(head_frame, background="white", text="Browse Files", border=0, fg="#00dfc0", cursor="hand2", command=Browse_PDF)
    pdf_file_path_browse_button.place(x=270, y=90)
    
    ## ## ## Encrypted PDF File ## ## ##
    
    en_pdf_file_path_label = Entry(head_frame, width=45, border=0, font=("Microsoft YaHei light", "10", "bold"))
    en_pdf_file_path_label.place(x=10, y=130)
    en_pdf_file_path_label.insert(0, "Enter the destination of the secured PDF")
    en_pdf_file_path_label.bind("<FocusIn>", on_enter_ENPDFPATH)
    en_pdf_file_path_label.bind("<FocusOut>", on_leave_ENPDFPATH)
    
    en_pdf_file_path_label_cursor_frame = Frame(head_frame, width=355, height=1.4, background="black")
    en_pdf_file_path_label_cursor_frame.place(x=10, y=155)
    
    en_pdf_file_path_browse_label = Label(head_frame, width=40, background="white", text="Don't you want to manually enter the path?")
    en_pdf_file_path_browse_label.place(x=-10, y=160)
    
    en_pdf_file_path_browse_button = Button(head_frame, background="white", text="Browse Directories", border=0, fg="#00dfc0", cursor="hand2", command=Browse_Dir)
    en_pdf_file_path_browse_button.place(x=250, y=160)
    
    ## ## ## Password which use to unlock the PDF ## ## ##
    
    en_pdf_file_password = Entry(head_frame, width=45, border=0, font=("Microsoft YaHei light", "10", "bold"))
    en_pdf_file_password.place(x=10, y=200)
    en_pdf_file_password.insert(0, "Enter the password you use to unlock the PDF here")
    en_pdf_file_password.bind("<FocusIn>", on_enter_PWD)
    en_pdf_file_password.bind("<FocusOut>", on_leave_PWD)
    
    en_pdf_file_pwd_cursor_frame = Frame(head_frame, width=355, height=1.4, background="black")
    en_pdf_file_pwd_cursor_frame.place(x=10, y=225)
    
    en_pdf_file_pwd_hint = Label(head_frame, width=35, background="white", text="Use this password to unlock your PDF.")
    en_pdf_file_pwd_hint.place(x=10, y=230)
    
    ###
    
    show_password_button = Button(head_frame, background="white", text="Show Password", border=0, fg="#00dfc0",cursor="hand2", command=show_password)
    show_password_button.place(x=240, y=230)
    
    #####################################################################################################################
    
    retype_passwd = Entry(head_frame,bg="white", border=0, width=45,font=("Microsoft Yahei light", "10", "bold"))
    retype_passwd.place(x=10, y=270)
    retype_passwd.insert(0, "Re-type the password")
    retype_passwd.bind("<FocusIn>", on_enter_REPASS)
    retype_passwd.bind("<FocusOut>", on_leave_REPASS)

    retype_passwd_cursor_frame = Frame(head_frame, width=355, height=1.4, background="black")
    retype_passwd_cursor_frame.place(x=10, y=295)




    Crypt_The_PDF_Button = Button(head_frame, text="Protect your PDF file", border=0, width=50, height=2, cursor="hand2", bg="#00dfc0", fg="white",font=("Microsoft Yahei light", "8", "bold"), command=Crypt_The_Pdf)
    Crypt_The_PDF_Button.place(x=10, y=340)
    
    mpage.mainloop()

if __name__ == "__main__":
    mainpage()