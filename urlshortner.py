import pyshorteners

def urlshorter():
    url = input("Enter your URL here: ")
    s = pyshorteners.Shortener()
    newurl = s.tinyurl.short(url)
    print(f"Shortned URL: {newurl}")
urlshorter()

choice= input("Do you want to short another URL (y/n)? ")

while choice.lower() == "y" or choice == "Y":
    urlshorter()
    choice = input("Do you want to short another URL (y/n)? ")
print("Thank you for using URL Shortner")
quit()

