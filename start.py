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

        # Create the canvas widget 
        self.canvas = tk.Canvas(self, width=500, height=400, background='gray75')
        

        #create the shape 
        self.canvas.create_rectangle(100, 75, 400, 300, fill='red')
        """ replace create lines with create polygon
        self.canvas.create_line(100, 75, 150, 50)
        self.canvas.create_line(150, 50, 350, 50)
        self.canvas.create_line(350, 50, 400, 75)
        """ 
        self.canvas.create_polygon(100, 75, 150, 50, 350, 50, 400, 75, fill='#000', outline='red2')
        self.canvas.pack(side="left" )

      
        

        self.quit = tk.Button(self, text="QUIT", fg="blue",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        if(self.color_flag):
           self.hi_there.config(fg="red")
           self.quit.config(bg="black") 
           self.color_flag = False
           coord = 10, 10, 300, 300
           arc = self.canvas.create_arc(coord, start=0,extent=150, fill='blue')
           self.canvas.pack(side="left" )           
        else:
           self.hi_there.config(fg="black")
           self.quit.config(bg="red")
           self.color_flag = True
           coord = 10, 10, 300, 300
           arc = self.canvas.create_arc(coord, start=0,extent=150, fill='green2')
           self.canvas.pack(side="left" )

 
root = tk.Tk()
app = Application(master=root)
app.mainloop()
