from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.title("Mini quiz")
fenetre.resizable(False, False)


frm = ttk.Frame(fenetre, padding=250)
frm.grid()



q = [
    {
        "laquestion": "Quelle est la capitale de la France ?",
        "choix": ["Paris", "Lyon", "Jupiter", "93"],
        "reponse": ["Paris"]
    },
    {
        "laquestion": "Qui a cree Amazone ?",
        "choix": ["Jeff Bezos", "Elon Musk", "Moi", "Bruno Amazone"],
        "reponse": ["Jeff Bezos"]
    },
    {
        "laquestion": "1 + 1² = ? ",
        "choix": ["11", "2", "2²", "3"],
        "reponse": ["2"]
        },
    { 
        "laquestion": "Quesque est une Tomate ?",
        "choix": ["Produit Laitier", "Viande", "Fruit", "Legume"],
        "reponse": ["Legume" , "Fruit"]
        },
    { 
        "laquestion": "la terre est-il plate ?",
        "choix": ["Oui", "Oui mais", "Non", "Je ne sais pas"],
        "reponse": ["Non"]
        },

]

pts = 0
numero_de_la_question = 0
blocreponse = 1
reponsecoche = []
case = []

for n in q[0]["choix"]:
    Variabletemporaire = IntVar()
    leschoix = Checkbutton(frm, text=n, variable=Variabletemporaire)
    leschoix.grid(column=0, row=blocreponse , padx=3, pady=3)
    blocreponse += 1
    reponsecoche.append(Variabletemporaire)
    case.append(leschoix)



def Valider():
    button1.config(state= DISABLED)
    vrai = True
    for indicedeschoixdeq, valider in enumerate(reponsecoche):
        print(valider.get())
        if(valider.get() == 0 and q[numero_de_la_question]["choix"][indicedeschoixdeq] in q[numero_de_la_question]["reponse"]):
            vrai = False
        elif(valider.get() == 1 and q[numero_de_la_question]["choix"][indicedeschoixdeq] not in q[numero_de_la_question]["reponse"]):
            vrai = False
    if(vrai):
        print("Correte")
        global pts
        pts += 1
        nbrpoint.configure(text="Points : " + str(pts))
        print(pts)
    else:
        print("Faux")
    
def Suivant():
    for c in case:
        c.destroy()

    case.clear()
    button1.config(state = NORMAL)
    global numero_de_la_question

    numero_de_la_question += 1

    Question.config(text=q[numero_de_la_question]["laquestion"])
    afficher_choix()
    
def afficher_choix():
    global blocreponse
    global reponsecoche
    global case

    blocreponse = 1
    reponsecoche = []
    
    for n in q[numero_de_la_question]["choix"]:
        Variabletemporaire = IntVar()

        leschoix = Checkbutton(frm, text=n, variable=Variabletemporaire)
        leschoix.grid(column=0, row=blocreponse, padx=3, pady=3)

        blocreponse += 1

        reponsecoche.append(Variabletemporaire)
        case.append(leschoix)




Question = ttk.Label(frm, text=q[0]["laquestion"] , background="white", font=("Arial", 14))

nbrpoint = Label(frm , text="Points : " + str(pts) , )
button1 = Button(frm, text="Valider" , command=Valider)
button2 = Button(frm, text="Suivant" , command=Suivant)
button3 = Button(frm, text="Quitter", command=fenetre.destroy)


Question.grid(column=0, row=0 , padx=25, pady=25)
nbrpoint.grid(column=0 , row=7)
button1.grid(column=0, row= 8)
button2.grid(column=0, row=9)
button3.grid(column=0, row=10)




fenetre.mainloop()
