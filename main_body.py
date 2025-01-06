import qrcode
import tkinter
import turtle

try:
    name = str(input("Please enter your name: "))
    url = str(input("Please enter your url"))
except KeyboardInterrupt:
    print("\nInput was interrupted. Exiting the program.")
    exit()
def type_validation(name,url):
    if type(name) == str and type(url) == str:
        return True
    else:
        return False
    
if type_validation:
    your_qr = qrcode.make(url)
    type(your_qr)
    your_qr.save("Your_QrCode.png")
