# importul bibliotecii webbrowser ce permite interactiunea cu browser-ul
import webbrowser as wb
# importul biblioteci tkinter
from tkinter import *

# crearea ferestrei de baza
root = Tk()

#setarea titlului ferestrei de baza
root.title("OpenGoogle")

#setarea dimensiunilor ferestrei de baza
root.geometry("300x200")

#crearea functiei ce ar permite deschiderea browserului
def google():
    # deschiderea paginii google in browser
    wb.open("www.google.com")

# crearea butonului ce apeleaza functia de deschidere a browser-ului
buton=Button(root, text="Open Google", command=google)

# plasarea butonului in ferestra
buton.pack(pady=50)

# crearea buclei de afisare continua a ferestrei
root.mainloop()