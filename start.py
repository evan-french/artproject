import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.color_flag = False

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["fg"] = "green"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="blue",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        if(self.color_flag):
           self.hi_there.config(fg="red")
           self.quit.config(bg="black")
           self.color_flag = False
        else:
           self.hi_there.config(fg="black")
           self.quit.config(bg="red")
           self.color_flag = True 

 
root = tk.Tk()
app = Application(master=root)
app.mainloop()
