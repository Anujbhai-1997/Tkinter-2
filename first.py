from tkinter import *
import tkinter.font
from PIL import ImageTk, Image    # install pillow    

root = Tk()
root.geometry('800x480')
root.title("TItel")
#root.iconbitmap(#Path to icon file - 16*16 or 32*32 pixel)
myFont = tkinter.font.Font(family='Courier New')
#Buttons
def quit():
    l = Label(root, text=e.get())
    l.grid(row=2, column=0)

button = Button(root, text = "Connect", command = quit, width = 15, height=2)
button.configure(bg="grey", fg="white", activebackground = "#33B5E5", relief = FLAT, anchor=CENTER, activeforeground="white", state=DISABLED)
button["bg"] = "#3298DB"
button["state"] = "normal"
button["font"] = myFont
button.grid(row=2, column=1)

#Entry
e = Entry(root)
e.grid(row=0, column=0, columnspan = 2)
e.insert(0, "Hallo")
#e.get()

#images
img = ImageTk.PhotoImage(Image.open("Images/AddTask.PNG"))
label = Label(image=img)
label.grid(row=3, column=0)


root.mainloop()


#class MainApplication(tk.Frame):
#    def __init__(self, parent, *args, **kwargs):
#        tk.Frame.__init__(self, parent, *args, **kwargs)
#        self.parent = parent
#        self.button = tk.Button(root, text="123", state=DISABLED)

        #<create the rest of your GUI here>

#if __name__ == "__main__":
#    root = tk.Tk()
#    MainApplication(root).pack(side="top", fill="both", expand=True)
#    root.mainloop()


#    class Navbar(tk.Frame): ...
#class Toolbar(tk.Frame): ...
#class Statusbar(tk.Frame): ...
#class Main(tk.Frame): ...

#class MainApplication(tk.Frame):
#    def __init__(self, parent, *args, **kwargs):
#        tk.Frame.__init__(self, parent, *args, **kwargs)
#        self.statusbar = Statusbar(self, ...)
#        self.toolbar = Toolbar(self, ...)
#        self.navbar = Navbar(self, ...)
#        self.main = Main(self, ...)

#        self.statusbar.pack(side="bottom", fill="x")
#        self.toolbar.pack(side="top", fill="x")
#        self.navbar.pack(side="left", fill="y")
#        self.main.pack(side="right", fill="both", expand=True)