# importul bibliotecilor
from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer

# crearea ferestrei root
root=Tk()

# setarea titlului ferestrei
root.title('Music player')

# setarea dimensiunilor ferestrei
root.geometry('370x300')

# blocare redimensionarii ferestrei
root.resizable(0,0)

# setarea culorii ferestrei
root.config(bg="#228B22")

# initierea pachetului mixel pentru lucru cu muzica
mixer.init()

# crearea functiei de incarcare a cantecelor
def add_songs():
    """
    Functia de incarcarea mai multor cantece in playlist
    """
    # adaugarea cantecelor prin deschiderea directoriului
    songs=filedialog.askopenfilenames(initialdir="/", title='Adaugare cantece', filetypes=(('mp3 Files' , '*.mp3'),))
    # se selecteaza primul cantec din lista de cantece
    song_0 = songs[0]
    # se creaza o lista in urma divizarii directorului dupa simbolul /
    lista = song_0.split("/")
    # se creaza o variabila globala care va reprezenta calea catre folderul cu cantece
    global path
    # se creaza calea din uniunea cu ajutorul simbolului / a tuturor elemtelor liste exceptandul pe ultimul
    path="/".join(lista[0:len(lista)-1])+"/"
    # se formeaza o bucla cu care se trece prin lista de cantece
    for song in songs:
        # selectarea denumirii cantecului din directoriu cartre acesta
        songs1 = song.replace(path, '').replace(".mp3", '')
        # fixarea cantecelor in lista cu cantece
        cantec_list.insert(END,songs1)
        # se activeaza primul cantec din lista
        cantec_list.selection_set(0)

# crearea functiei de pornirea cantecului selectat
def play_song():
    """
    Functia de pornire a cantecului selectat
    """
    # verificare daca playlist-ul nu este gol
    if cantec_list.size() == 0:
        # se afiseaza mesajul de atentionare
        messagebox.showinfo(title='Informație' , message="Nu ați incarcat nici un cântec")

    # Variabila ce specifica ca cantecul este pe pauza se seteaza in false
    global paused
    paused = False

    # alegerea cantecului selectat
    song=cantec_list.get(ACTIVE)
    # adaugarea intregului directoriu catre cantec
    song = f'{path}{song}.mp3'
    # incarcarea cantelului
    mixer.music.load(song)
    #pornirea cantecului
    mixer.music.play(loops=0)

# crearea functiei de oprire a cantecului
def stop_song():
    """
    Functia de oprire a cantecului
    """
    # verificare daca playlist-ul nu este gol
    if cantec_list.size() == 0:
        # se afiseaza mesajul de atentionare
        messagebox.showinfo(title='Informație' , message="Nu ați incarcat nici un cântec")
    # oprirea cantecului
    mixer.music.stop()

# se creaza o variabila globala ce va fixa faptul ca cantecul este pe pauza
paused=False

# crearea functiei de punere in pauza a cantecului
def pause_song():
    """
    Functia de pauzare a cantecului
    """
    # verificare daca playlist-ul nu este gol
    if cantec_list.size() == 0:
        # se afiseaza mesajul de atentionare
        messagebox.showinfo(title='Informație' , message="Nu ați incarcat nici un cântec")
    #verificarea daca cantecul este pe pauza
    global paused
    if paused==True:
        # cantecul se scoate de pe pauza
        mixer.music.unpause()
        # se specifica ca cantecul nu mai e pe pauza
        paused = False
    # se verifica daca cantecul nu este pe pauza
    else:
        # cantecul se scoate de pe pauza
        mixer.music.pause()
        # se specifica ca cantecul e pe pauza
        paused = True

# crearea unui functii de stergere a tuturor cantecelor din playlist
def del_songs():
    """
    Functia de stergere a tuturor cantecelor din playlist
    """
    # oprirea cantecului care canta la moment
    stop_song()
    # stergerea tuturor cantecelor
    cantec_list.delete(0,END)

# crearea unui buton de incarcare a cantecelor in playlist
buton_incarc = Button(root, text="Încărcare cântece", bg="blue", fg="white", command=add_songs)
buton_incarc.grid(row=0, column=0, columnspan=3, pady=5)

# crearea unui buton de sterege a cantecelor din playlist
buton_sterg = Button(root, text="Stergere cântece", bg="blue", fg="white", command=del_songs)
buton_sterg.grid(row=1, column=0, columnspan=3, pady=5)

# crearea unui listbox pentru playlist
cantec_list=Listbox(root, width=60, bg="#9ACD32", fg="#0000FF", selectbackground='#B22222')
#fixarea playlist-ului in fereastra
cantec_list.grid(row=2, column=0, columnspan=3, pady=5, padx=3)

# crearea butonului de start
buton_start = Button(root, text="Start", bg="green",fg="white", command=play_song)
buton_start.grid(row=3, column=0, pady=5)

# crearea butonului de pauza
buton_pauza = Button(root, text="Pauza",bg="yellow", command=pause_song)
buton_pauza.grid(row=3, column=1, pady=5)

# crearea butonului de stop
buton_stop = Button(root, text="Stop", bg="red",fg="white", command=stop_song)
buton_stop.grid(row=3, column=2, pady=5)

# crearea buclei de afisare permanenta
root.mainloop()