import qrcode

def qrgenerator():
    value = input("Enter your Value: ")

    qr_img = qrcode.make(value)
    qr_img.show()
    qr_img.save("qrcode.png")

qrgenerator()

choice = input("Do you want to generate another QR code (y/n)? ")

while choice.lower() == "y" or choice == "Y":
    qrgenerator()
    choice = input("Do you want to generate another QR code (y/n)? ")

print("Thank you for using QR Generator")
quit()
