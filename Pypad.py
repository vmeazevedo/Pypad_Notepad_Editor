from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    root=Tk()

    width = 200
    height = 300
    Textarea=Text(root)
    Menubar=Menu(root,activebackground="purple",activeforeground="white",bg="pink",fg="black")
    filemenu=Menu(Menubar, tearoff=0,activebackground="purple",activeforeground="white")
    editmenu=Menu(Menubar, tearoff=0,activebackground="purple",activeforeground="white")
    helpmenu=Menu(Menubar, tearoff=0,activebackground="purple",activeforeground="white")

    scrollbar = Scrollbar(Textarea,activebackground="pink",bg="pink")
    file=None


    def __init__(self, **kwargs):

    #Seting window size
        try:
            self.width=kwargs['widths']
        except KeyError:
            pass
        try:
            self.height=kwargs["heights"]
        except KeyError:
            pass

    #Window text
        self.root.title("Pypad v1.0 - Notepad")
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        left=(screenwidth/2) - (self.width/2)
        top=(screenheight/2)- (self.height/2)
        self.root.geometry('%dx%d+%d+%d'%(self.width,self.height,left,top))

    #To make the text area auto resizable
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(0, weight=2)
        self.Textarea.grid(sticky = N+E+S+W)

        #To open a new file and open and save
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command = self.savefile)
        self.filemenu.add_command(label="Save as", command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.exitapp)
        self.Menubar.add_cascade(label="File", menu=self.filemenu)

        #Edit Menu
        self.helpmenu.add_command(label="About Pypad",command=self.showhelp)
        self.Menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.Menubar)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.Textarea.yview)
        self.Textarea.config(yscrollcommand=self.scrollbar.set)

#Functions
    def exitapp(self):
        self.root.destroy()

    def showhelp(self):
        showinfo("PyPad", "Created by Vinícius Azevedo")

    def openfile(self):
        self.file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.file =="":
            self.file= None
            print("EMPTY")
        else:
            self.root.title(os.path.basename(self.file[:-4]) + " --Notepad")
            self.Textarea.delete(1.0 , END)
            file=open(self.file, "r")
            self.Textarea.insert(1.0, file.read())
            file.close()

    def newfile(self):
            self.root.title("Pypad v1.0 - Notepad")
            self.file = None
            self.Textarea.delete(1.0,END)

    def savefile(self):
        if self.file == None:
            self.file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if self.file == "":
                self.file =None
            else:
                file = open(self.file,"w")
                file.write(self.Textarea.get(1.0,END))
                file.close()
                self.root.title(os.path.basename(self.file)+"- Notepad")
        else:
            file=open(self.file, "w")
            file.write(self.Textarea.get(1.0,END))
            file.close()

    def saveasfile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.file=='':
                self.file=None
            else:
                file=open(self.file,"w")
                file.write(self.Textarea.get(1.0,END))
                file.close()
                self.root.title(os.path.basename(self.file)+"- Notepad")
        else:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            file = open(self.file, "w")
            file.write(self.Textarea.get(1.0, END))
            file.close()
            self.root.title(os.path.basename(self.file) + "- Notepad")

    def run(self):
        self.root.mainloop()

notepad=Notepad(widths=600, heights=500)
notepad.run()