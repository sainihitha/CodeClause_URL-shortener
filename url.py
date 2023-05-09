import pyshorteners
url=input("Enter the link here: ")
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(url)
print("Shorten link: "+x)
