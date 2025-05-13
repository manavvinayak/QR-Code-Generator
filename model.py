import pyqrcode
import png
from pyqrcode import QRCode
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.title("QR Code Generator")
window.geometry('400x450')

Label(window, text='Let\'s create QR code', font='Georgia 15' ).pack(pady=10) 


s = StringVar()

# taking input
Entry(window, textvariable=s, font='Helvetica 15').pack(pady=10)

# QR code generator function
def create_qrcode():
    s1 = s.get()
    if s1.strip() == "":
        Label(window, text="Please enter some text!", font = 'Georgia 15', fg="red").pack()
        return
    qr = pyqrcode.create(s1)
    qr.png('generatedQR.png', scale=6)
    Label(window, text='QR code generated successfully!',font = 'Garamond 15', fg="green").pack()
    
     # Load and display the image
    img = Image.open("generatedQR.png")
    img = img.resize((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    qr_image_label = Label(window)
    qr_image_label.pack(pady=10)
    qr_image_label.config(image=img_tk)
    qr_image_label.image = img_tk  

# Button
Button(window, text='Create ', bg='green',font ='Georgia 13', fg='white', command=create_qrcode).pack(pady=20)

# Start the GUI loop
window.mainloop()
