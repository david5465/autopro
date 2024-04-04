import tkinter as tk
import sys

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)

def main():
    root = tk.Tk()
    root.title("Consola a Tkinter")

    text_area = tk.Text(root)
    text_area.pack(expand=True, fill=tk.BOTH)

    # Redirigir la salida de la consola al widget Text
    sys.stdout = ConsoleRedirector(text_area)

    print("¡Hola desde la consola!")
    print("gg")

    root.mainloop()

if __name__ == "__main__":
    main()
