import qrcode 

title = input()
url = str(input())

def making_qr(url, title):
    qr_save = qrcode.make(url)
    qr_save.save("qr-img.jpg")  
    
    return qr_save
    
def qr_saved():
    return qr_saved 

making_qr("Youtube", "Welcome to Youtube")
#making a saved qr in the directory

def output():
    return none 

def main_output():
    return x
