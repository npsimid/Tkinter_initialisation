# importul bibliotecilor
from pytube import YouTube
from tkinter import *
from tkinter import messagebox, filedialog

# crearea ferestrei root
root = Tk()

# setarea titlului ferestrei
root.title("Descărcător Youtube")

# setarea dimensiunilor ferestrei
root.geometry("400x290")

# blocare redimensionarii ferestrei
root.resizable(0,0)

# setarea culorii ferestrei
#root.config(bg="#34ab67")

# definirea functiei de incarcare a materialului video (se va apela la apararea butornului de incarcare)
def load_func():
    """Functia ce incarca materialul video, extrage informatiile despre acesta si le afiseza"""

    #introducerea blocului try-except pentru a evita aparaiti erorilor in cazul in care nu se introduce link
    # sau se introduce un link gresit
    try:
        # formarea unei variabile globale yt care ar pute fi apelata si in afara functie
        global yt
        #crearea unui obiect al calsi Youtube
        yt = YouTube(entry_link.get())

        # inscriera informatiei despre datele clipului in label-urile corespunzatoare
        label_titlu_v.config(text=yt.title)
        label_lung_v.config(text=f"{yt.length//60}:{yt.length%60}") # sa transformat timpul din secunde in minute
        label_autor_v.config(text=yt.author)
        label_data_v.config(text= yt.publish_date)
        label_vizual_v.config(text=yt.views)
        label_rating_v.config(text=yt.rating)

        # activarea label-urilor de descriere a informatie afisate
        label_titlu_t.grid(row=4, column=0, sticky=E, padx=5)
        label_lung_t.grid(row=5, column=0, sticky=E, padx=5)
        label_autor_t.grid(row=6, column=0, sticky=E, padx=5)
        label_data_t.grid(row=7, column=0, sticky=E, padx=5)
        label_vizual_t.grid(row=8, column=0, sticky=E, padx=5)
        label_rating_t.grid(row=9, column=0, sticky=E, padx=5)

        # activarea label-urilor cu informatie despre clip
        label_titlu_v.grid(row=4, column=1, sticky=W, padx=5)
        label_lung_v.grid(row=5, column=1, sticky=W, padx=5)
        label_autor_v.grid(row=6, column=1, sticky=W, padx=5)
        label_data_v.grid(row=7, column=1, sticky=W, padx=5)
        label_vizual_v.grid(row=8, column=1, sticky=W, padx=5)
        label_rating_v.grid(row=9, column=1, sticky=W, padx=5)

        # activare butornului de descarcare
        button_save.grid(row=10, column=0, columnspan=2, pady=5)

    except:
        # Afisare unei ferestre de atentionare cu mesajul neintroducerii sau introducerii grsite a linkului
        messagebox.showinfo(title="Atentie", message="Nu ati introdus link Youtube sau ati introdus un link gresit ")

# definirea functiei de descarcare a materialului video (se va apela la apararea butornului de descarcare)
def download_func():
    """Functia ce descarcare a materialul video in folderul dorit"""

    # introducerea blocului try-except pentru a evita aparitia erorilor datorate descarcarii
    try:
        #selectarea folderului unde se va salva clipul
        path = filedialog.askdirectory(initialdir="/", title="Save file")
        #selectare fluxului din clip care se va salva
        yts = yt.streams.filter(file_extension="mp4", progressive="True").order_by("resolution").desc().first()
        # salvarea fluxului selectat in folderul selectat
        yts.download(path)
        #Inscrierea informatiei de realizare cu suces a operatie de salvare in label-ul corespunzator
        label_rez.config(text="Descărcare cu succes!!!")
        # activarea labelului ce va informa despre statutul operatie de salvare
        label_rez.grid(row=11, column=0, columnspan=2, pady=5)
    except:
        # Inscrierea informatiei de esuarea a operatie de salvare in label-ul corespunzator
        label_rez.config(text="Descărcarea a esuat")
        # activarea labelului ce va informa despre statutul operatie de salvare
        label_rez.grid(row=11, column=0, columnspan=2, pady=5)

# crearea unui label in care ni se va cere sa introducem link-ul Youtube
label_intro = Label(root, text="Introduceți link-ul Youtube")
# activarea labelului in celula din randul 0, coloana 0 dar se va intinde pe 2 coloane
# continutul va si deplasat de la margini pe orizontal (padx) si pe vertical (pady) cu 5 si va fi plasat din stanga (W=vest)
label_intro.grid(row=0, column=0, columnspan=2, pady=5, sticky=W, padx=5)

# crearea unui entry in care se va introduce link-ul Youtube
entry_link = Entry(root, width=64)
# activarea entry-ului in celula din randul 1, coloana 0
entry_link.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

# crearea unui buton care va incarca clipul apeland functia load_func
button_load = Button(root, text="Încărcare video", command=load_func)
# activarea butonului in celula din randul 2, coloana 0
button_load.grid(row=3, column=0, columnspan=2, pady=5)

# crearea unor labelui prin intermediul carora se va specifica ce informatie despre clip se afiseaza
label_titlu_t = Label(root, text="Denumirea clipului:")
label_lung_t = Label(root, text="Lungimea clipului:")
label_autor_t = Label(root, text="Autorul clipului:")
label_data_t = Label(root, text="Data publicarii:")
label_vizual_t = Label(root, text="Numarul de vizualizari:")
label_rating_t = Label(root, text="Rating-ul piesei:")

# crearea unor labelui prin intermediul carora se va afisa informatiile despre clip
label_titlu_v = Label(root)
label_lung_v = Label(root)
label_autor_v = Label(root)
label_data_v = Label(root)
label_vizual_v = Label(root)
label_rating_v = Label(root)

# crearea unui buton care va descarca clipul apeland functia download_func
button_save = Button(root, text="Descărcare video", command=download_func)
# crearea unui label in care se va afisa statutul operatie de salvare
label_rez = Label(root)

# crearea buclei de afisare permanentaa ferestrei
root.mainloop()