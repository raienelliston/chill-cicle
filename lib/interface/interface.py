import tkinter as tk

class Interface(tk.Frame):
    def __init__(self) -> None:
        Interface.root = tk.Tk()
        Interface.root.title("Interface")
        Interface.root.geometry("800x480")

        Interface.root.label = tk.Label(Interface.root, text = "Hello World!")
        Interface.root.label.pack(padx=20, pady=20)

    def setup(self) -> None:
        None

    def addElement(self, element) -> None:
        None

    def loop(self) -> None:
        Interface.root.mainloop()

    def __del__(self) -> None:
        None

if __name__ == "__main__":
    Interface = Interface()
    if True:
        Interface.loop()