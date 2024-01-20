from tkinter import *
import requests
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/"
page=requests.get(url)
Soup=BeautifulSoup(page.content,"html.parser")
info = Soup.find_all(class_="maincounter-number")
a=[items.get_text() for items in info]

country=""

root=Tk()
root.title("corona reports")
root.geometry("500x500")

font=("helvetica",12,"bold")

def find_info():
    country=c.get()
    url1='https://www.worldometers.info/coronavirus/country/'+country

    page1=requests.get(url1)
    Soup1=BeautifulSoup(page1.content,"html.parser")
    info1=Soup1.find_all(class_="maincounter-number")
    b=[items.get_text() for items in info1]

    label1=Label(root,font=font,text="Total cases of corona virus in "+country)
    label1.pack()
    label1=Label(root,font=font,text=b[0])
    label1.pack()


    label1=Label(root,font=font,text="Deths of coronavirus in "+country)
    label1.pack()
    label1=Label(root,font=font,text=b[1])
    label1.pack()

    label1=Label(root,font=font,text="total recovered people from corona virus in "+country)
    label1.pack()

    label1=Label(root,font=font,text=b[2])
    label1.pack()

label1=Label(root,font=font,text="Total cases of corona virus")
label1.pack()
label1=Label(root,font=font,text=a[0])
label1.pack()


label1=Label(root,font=font,text="Deths of coronavirus")
label1.pack()
label1=Label(root,font=font,text=a[1])
label1.pack()

label1=Label(root,font=font,text="total recovered people from corona virus")
label1.pack()

label1=Label(root,font=font,text=a[2])
label1.pack()

label1=Label(root,font=font,text="select country name: ")
label1.pack()
c=Entry(root,font=font)
c.pack()

Button1=Button(root,font=font,text="find info",bg="green",command=find_info)
Button1.pack()

root.mainloop()
