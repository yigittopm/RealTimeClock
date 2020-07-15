  
import tkinter
from time import strftime

top = tkinter.Tk()
top.title('Clock')
top.resizable(666,155)

def time(): 
    string = strftime('%H:%M:%S %p') 
    clockTime.config(text = string) 
    clockTime.after(1000, time)


clockTime = tkinter.Label(top, font = ('calibri', 40, 'bold'), background = 'lightBlue', foreground = 'white')

clockTime.pack(anchor = 'center')
time() 


top.mainloop()