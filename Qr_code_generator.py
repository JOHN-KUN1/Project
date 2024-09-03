import tkinter as tk
from tkinter import font
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
import qrcode

print("hello")

# Create the main window
window = tk.Tk()

window.geometry("700x400")
window.resizable(False,False)
window.title("QR CODE GENERATOR")
window["bg"] = "#2b2929"

#Title section
title_font = font.Font(size = 24,weight="bold")
title = tk.Label(window, text="QR CODE GENERATOR",font=title_font,pady=20,fg="pink",bg= "#2b2929")
title.pack()

#function on submit
def generateQrCode():
    username = usernameEntry.get()
    department = departmentEntry.get()
    fileNo = fileNumberEntry.get()

    data = f"Name: {username}\n Department: {department}\n File Number: {fileNo}"
    img = qrcode.make(data)
    img.save("qrcode.png")


#label Section
label_name_font = font.Font(size=18)
label_name = tk.Label(window, text="Name:",fg="white",justify="left",font=label_name_font,bg="#2b2929")
label_name.place(x=100,y=100)

#Entry for label name
usernameEntry = Entry(window,width=36)
usernameEntry.place(x=175,y=107)

#label department
label_department_font = font.Font(size=18)
label_department = tk.Label(window, text="Department:",fg="white",justify="left",font=label_department_font,bg="#2b2929")
label_department.place(x=100,y=150)

#Entry for label department

departmentEntry = Entry(window,width=40)
departmentEntry.place(x=240,y=155)

#label for file number
label_fileNumber_font = font.Font(size=18)
label_fileNumber = tk.Label(window, text="File Number:",fg="white",justify="left",font=label_fileNumber_font,bg="#2b2929")
label_fileNumber.place(x=100,y=200)

#Entry for label file number
fileNumberEntry = Entry(window,width=40)
fileNumberEntry.place(x=245,y=205)


#Button Submit
submit_button = Button(text="Submit",bg="pink",command=generateQrCode)
submit_button.place(x=300,y = 245)

def show_message_info():
    messagebox.showinfo("Information","The Qr Code images will be saved on your PC with the name 'qrcode.png'. Please ensure that the application is running inside a new folder on your desktop ")



# Run the application
window.after(1000,show_message_info)
window.mainloop()

