from tkinter import *
from playsound import playsound

from pygame import *
mixer.init()



root = Tk()
root.title("LaminePiano v1.0 (beta)")


#les foncions de son
def play1 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\do.wav")
    sound.play()

def play2 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\re.wav")    
    sound.play()

def play3 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\mi.wav")    
    sound.play()
def play4 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\fa.wav")    
    sound.play()
def play5 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\so.wav")    
    sound.play()
def play6 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\la.wav")    
    sound.play()
def play7 ():   
    sound=mixer.Sound("C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\sound\\si.wav")    
    sound.play()

root.geometry ("900x450")


lion = PhotoImage (file = "C:\\Users\\johnp\\OneDrive\\Bureau\\piano\\images\\bg.png")
bg=Label (root, image=lion)
bg.place (x=0 , y=0 , relwidth=1 , relheight=1)


i=150-30
#les bouttons de piano
key1=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play1)
key1.place(x=30,y=120)

key2=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play2)
key2.place(x=150,y=120)

key3=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play3)
key3.place(x=270,y=120)

key4=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play4)
key4.place(x=390,y=120)

key5=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play5)
key5.place(x=510,y=120)

key6=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play6)
key6.place(x=630,y=120)

key7=Button(root, height = 20, width =15 , borderwidth=3 , bg="white" , command=play7)
key7.place(x=750,y=120)


tit= Label(root , text = " The Wooden Piano ", font=("Beta Dance ",30 ), bg="black" , fg="darkgoldenrod" )
tit.place(x=260 , y=35)









root.mainloop()
