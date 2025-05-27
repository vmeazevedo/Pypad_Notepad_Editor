import os
import tkinter as tk
from tkinter import messagebox, filedialog

class Notepad:
    def __init__(self, width=600, height=500):
        # Janela principal
        self.root = tk.Tk()
        self.root.title("PyPad v1.0 - Notepad")

        self.width = width
        self.height = height
        self.file = None

        # Centralizar janela na tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - self.width) / 2)
        y = int((screen_height - self.height) / 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

        # Área de texto + scrollbar
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # Menu
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root, bg="pink", fg="black", activebackground="purple", activeforeground="white")

        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0, activebackground="purple", activeforeground="white")
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # Menu Ajuda
        help_menu = tk.Menu(menubar, tearoff=0, activebackground="purple", activeforeground="white")
        help_menu.add_command(label="About PyPad", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    # Ações do menu
    def new_file(self):
        self.root.title("PyPad v1.0 - Notepad")
        self.file = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        filepath = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            self.file = filepath
            self.root.title(f"{os.path.basename(filepath)} - Notepad")
            with open(filepath, "r") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, f.read())

    def save_file(self):
        if not self.file:
            self.save_as_file()
        else:
            with open(self.file, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{os.path.basename(self.file)} - Notepad")

    def save_as_file(self):
        filepath = filedialog.asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            self.file = filepath
            with open(filepath, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{os.path.basename(filepath)} - Notepad")

    def exit_app(self):
        self.root.destroy()

    def show_about(self):
        messagebox.showinfo("About PyPad", "Created by Vinícius Azevedo")

    def run(self):
        self.root.mainloop()


# Execução
if __name__ == "__main__":
    app = Notepad(width=600, height=500)
    app.run()
