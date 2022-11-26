import tkinter
import tkinter.messagebox
import qrcode
from PIL import Image, ImageTk
import PyTouchBar

root = PyTouchBar.TouchBarTk()
root.title("QR Code Generator")
root.geometry("480x480")
root.minsize(480, 480)
root.maxsize(480, 480)


label = tkinter.Label(root, text="Enter the text to be converted into QR Code")
label.grid(row=0, column=0)

qrCodeTextVar = tkinter.StringVar()
qrcodeEntry = tkinter.Entry(root, width=50, textvariable=qrCodeTextVar)
qrcodeEntry.grid(row=1, column=0, padx=10, pady=3)

genQrCodeButton = tkinter.Button(root, text="Generate QR Code")
genQrCodeButton.grid(row=2, column=0, padx=10)

# place to show the QR Code
qrCodeLabel = tkinter.Label(root)
qrCodeLabel.grid(row=3, column=0, padx=10, pady=10)
qrCodeLabel.size = (300, 300)

def generateQRCode():
    qr = qrcode.make(qrCodeTextVar.get())
    # display the QR Code
    qrCodeLabel.image = ImageTk.PhotoImage(qr)
    qrCodeLabel.configure(image=qrCodeLabel.image)

genQrCodeTouchBarBtn = PyTouchBar.TouchBarItems.Button(title="Generate QR Code", action=lambda _: generateQRCode())
PyTouchBar.set_touchbar([genQrCodeTouchBarBtn])
genQrCodeButton.configure(command=generateQRCode)

root.mainloop()