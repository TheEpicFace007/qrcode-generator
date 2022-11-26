import tkinter
import tkinter.messagebox
import qrcode
from PIL import Image, ImageTk
import PyTouchBar
import tkinter.filedialog
import sys
import os

root = PyTouchBar.TouchBarTk()
root.title("QR Code Generator")
root.geometry("480x480")
root.minsize(480, 480)
root.maxsize(1000, 1000)


label = tkinter.Label(root, text="Enter the text to be converted into QR Code")
label.grid(row=0, column=0)

qrCodeTextVar = tkinter.StringVar()
qrcodeEntry = tkinter.Entry(root, width=50, textvariable=qrCodeTextVar)
qrcodeEntry.grid(row=1, column=0, padx=10, pady=3)

genQrCodeButton = tkinter.Button(root, text="Generate QR Code")
genQrCodeButton.grid(row=2, column=0, padx=10)

saveQrCodeButton = tkinter.Button(root, text="Save QR Code")
saveQrCodeButton.grid(row=3, column=0, padx=10)
def saveQrCode():
    qr = qrcode.make(qrCodeTextVar.get())
    homedir = os.path.expanduser('~')
    qr.save(tkinter.filedialog.asksaveasfilename(
            initialdir=homedir,
            filetypes=[("PNG", "*.png")], defaultextension=".png"),
        )
    
saveQrCodeButton.configure(command=saveQrCode)
saveQrCodeTouchBarButton = PyTouchBar.TouchBarItems.Button(title='Save QR Code', action=lambda _: saveQrCode())

# place to show the QR Code
qrCodeLabel = tkinter.Label(root)
qrCodeLabel.grid(row=4, column=0, padx=10, pady=10)
qrCodeLabel.size = (300, 300)

def generateQRCode():
    qr = qrcode.make(qrCodeTextVar.get())
    # display the QR Code
    qrCodeLabel.image = ImageTk.PhotoImage(qr)
    qrCodeLabel.configure(image=qrCodeLabel.image)

genQrCodeTouchBarBtn = PyTouchBar.TouchBarItems.Button(title="Generate QR Code", action=lambda _: generateQRCode())
genQrCodeButton.configure(command=generateQRCode)

PyTouchBar.set_touchbar([genQrCodeTouchBarBtn, saveQrCodeTouchBarButton])
root.mainloop()