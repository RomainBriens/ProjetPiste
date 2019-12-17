import importlib
try:
    importlib.import_module("cv2")
    importlib.import_module("PIL.Image")   
    importlib.import_module("PIL.ImageTk")    
except ImportError:
    import subprocess
    import sys
    print("\nIl manque des modules! Téléchargemnt en cours...")
    subprocess.Popen([sys.executable, "-m", "pip", "install", "opencv-python", "pillow"]).wait()
    print("Installation terminée!")
finally:
    globals()["cv2"] = importlib.import_module("cv2")
    globals()["PIL.Image"] = importlib.import_module("PIL.Image")
    globals()["PIL.ImageTk"] = importlib.import_module("PIL.ImageTk")

    import tkinter as tk
    import cv2
    import PIL.Image, PIL.ImageTk
    import time
    from tkinter import messagebox

frame = []
ret = False

class App:
    def __init__(self, window):
        self.window = window
        # self.window.title(window_title)
        self.video_source = 0
        self.freeze=False
        self.time = 0
        self.face = (0, 0, 0, 0)

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
        
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        
        self.window.mainloop()

    def unfreezeCam(self):
        self.time = 0
        self.freeze = False
 
    
    def envoyer_window(self, window_camera): #appuyer sur le bouton envoyer de la fenêtre window_camera pour afficher le message d'information
        messagebox.showinfo("INFORMATION", "Votre saisie a été enregistré") 
        self.unfreezeCam()
        window_camera.destroy()

    def update(self):
        global frame, ret
        # Get a frame from the video source
        def get_detected():
                        
            window_camera=tk.Tk()  
            window_camera.lift()                      
            window_camera.title("MESSAGE DE SECURITE")
            window_camera.resizable(width=False, height=False) # Permet de ne pas redimensionner manuellement la fenêtre 

            screen_X=int(window_camera.winfo_screenwidth())    # réccupération taille écran largeur (mm)
            screen_Y=int(window_camera.winfo_screenheight())   #réccupération taille écran hauteur (mm)

            X=500                                              #choix des dimensions de la fenêtre
            Y=300

            posX=(screen_X //2)-(X//2)                         # permet de centrer la fenêtre sur l'écran
            posY=(screen_Y//2)-(Y//2)

            geo1="{}x{}+{}+{}".format(X, Y, posX, posY)
            window_camera.geometry(geo1)

            # Dans cette partie du code nous allons créer les widgets de la fenêter window_camera

            camera_label=tk.Label(window_camera, text="UN COUTEAU A ETE DETECTE") #affiche un mesage sur une ligne 
            camera_label['fg']="red"                                       # choix de la couleur du texte
            camera_label.grid(padx=175 ,pady=15)

            Frame1=tk.LabelFrame(window_camera, text="Equipes à envoyer :", borderwidth=2, height=150, width=200)   # Création d'un cadre contenat des information, permet d'organiser interface
            Frame1.grid(row=1, column=0, pady=30)

            check_camera=tk.Checkbutton(Frame1, text="Envoyer une équipe d'intervention de sécurité")
            check_camera.grid(row=0, column=0)                           

            check_camera1=tk.Checkbutton(Frame1, text= "Envoyer une équipe de secours médical")
            check_camera1.grid(row=1, column=0, pady=5)

            # On créé le menu déroulant

            mainmenu=tk.Menu(window_camera) # permet de définir le menu principal

            def show_about():   # On définit une fonction qui ouvre une fenêtre secondaire
                window= Toplevel(window_camera,)
                window.title("Confirmer la station")
                label_window=Label(window, text="Confirmer la position")
                label_window.grid(padx=80, pady=10, row=0, column=0)
                button_window= Button(window, text="Confirmer", width=20)
                button_window.grid(pady=10, row=1, column=0)
                L=300
                H=100
                geo2="{}x{}+{}+{}".format(L,H,550,350)
                window.geometry(geo2)
            

                
            ligne_jaune=tk.Menu(mainmenu, tearoff=0) 

            ligne_jaune.add_command(label="4 cantons stade Pierre Mauroy", command=show_about)
            ligne_jaune.add_command(label="Cité scientifique",command=show_about)
            ligne_jaune.add_command(label="Triolo",command=show_about)
            ligne_jaune.add_command(label="Villeneuve d'ascq hôtel de ville",command=show_about)
            ligne_jaune.add_command(label="Pont de bois",command=show_about)
            ligne_jaune.add_command(label="Square flandre",command=show_about)
            ligne_jaune.add_command(label="Mairie d'hellemmes",command=show_about)
            ligne_jaune.add_command(label="Marbrerie",command=show_about)
            ligne_jaune.add_command(label="Cauliez",command=show_about)
            ligne_jaune.add_command(label="Gares Lille-Flandres",command=show_about)
            ligne_jaune.add_command(label="Rihour",command=show_about)
            ligne_jaune.add_command(label="République Beaux-Arts",command=show_about)
            ligne_jaune.add_command(label="Gambetta",command=show_about)
            ligne_jaune.add_command(label="Wazemmes",command=show_about)
            ligne_jaune.add_command(label="Porte des Postes",command=show_about)
            ligne_jaune.add_command(label="CHU Oscar-Lambret",command=show_about)
            ligne_jaune.add_command(label="CHU Eurasanté",command=show_about)


            ligne_rouge=tk.Menu(mainmenu, tearoff=0)

            ligne_rouge.add_command(label="Saint Philibert",command=show_about)
            ligne_rouge.add_command(label="Lomme-Lambersart-Arthur Notebart",command=show_about)
            ligne_rouge.add_command(label="Port de Lille",command=show_about)
            ligne_rouge.add_command(label="Montebello",command=show_about)
            ligne_rouge.add_command(label="Portes des Postes",command=show_about)
            ligne_rouge.add_command(label="Portes de Douai",command=show_about)
            ligne_rouge.add_command(label="Portes de Valenciennes",command=show_about)
            ligne_rouge.add_command(label="Portes d'Arras",command=show_about)
            ligne_rouge.add_command(label="Mairie de Lille",command=show_about)
            ligne_rouge.add_command(label="Gare Lille-Flandres",command=show_about)
            ligne_rouge.add_command(label="Saint-Maurice Pellevoisin",command=show_about)
            ligne_rouge.add_command(label="Les Près-Edgard-Pisani",command=show_about)
            ligne_rouge.add_command(label="Wasquehal-hôtel de ville",command=show_about)
            ligne_rouge.add_command(label="Mairie de Croix",command=show_about)
            ligne_rouge.add_command(label="Epeule Montesquieu",command=show_about)
            ligne_rouge.add_command(label="Eurotéléport",command=show_about)
            ligne_rouge.add_command(label="Tourcoing-centre",command=show_about)
            ligne_rouge.add_command(label="CH Drob",command=show_about)

            # On affiche les choix en cascade

            mainmenu.add_cascade(label="Ligne jaune", menu=ligne_jaune)
            mainmenu.add_cascade(label="Ligne rouge", menu=ligne_rouge)


            window_camera.config(menu=mainmenu) # affiche la barre du menu principal



            confiramtion_camera=tk.Button(window_camera, text="Envoyer", width=15, command=lambda : self.envoyer_window(window_camera))
            confiramtion_camera.grid(pady=15) 

            # window_camera.mainloop ()   #permet à la fenêtre de ne pas se refermer via une boucle infinie
        
        if self.time == 0 or time.clock() - self.time < 0.1:
            ret, frame = self.vid.get_frame()

        if not self.freeze:
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            self.faces = face_cascade.detectMultiScale(frame, 1.3, 5)

        for (x,y,w,h) in self.faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            if not self.freeze:
                self.time = time.clock()
                self.freeze=True
                get_detected()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

            self.window.after(self.delay, self.update)
        
        
class MyVideoCapture:
    def __init__(self, video_source=0):
         # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

        # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    # Create a window and pass it to the Application object


def get_Logins():
    # Ce programme va permettre d'ouvrir une fenêtre avec le message de sécurité et une fenêtre qui demandera ID et mp de l'agent de sécurité# 
    
    # création de la fenêtre d'identification de l'agent de sécurité

    security=tk.Tk()                         
    security.title("IDENTIFICATION WINDOW")
    security.resizable(False, False)
    security.lift()
    L=300                                             # choix de la taille de la fenêtre d'identification de l'agent de sécurité
    H=100

    geo2= "{}x{}+{}+{}".format(L,H,500,300)
    security.geometry(geo2)

    # Dans cette partie du code nous allons afficher les widgets nécessaire à la fenêtre de l'agent de sécurité


    security_label1=tk.Label(security, text="Entrer votre ID")
    security_label2=tk.Label(security, text="Entrer votre mot de passe")



    security_label1.grid(row=2)
    security_label2.grid(row=3)

    security_entry1=tk.Entry(security) # On définit les espaces de saisis des MP et ID
    security_entry2=tk.Entry(security, show="*") # Le mot de passe va afficher * peut importe le caractère saisie

    print(security_entry1) # imprimer la saisie dans la console --> à faire 
    print(security_entry2)

    security_entry1.grid(row=2, column=1,columnspan = 2)   #permet d'afficher sur la fenêtre les widgets ajoutés aux positions souhaitées
    security_entry2.grid(row=3, column=1,columnspan = 2)


    security_button=tk.Button(security, text="OK", width=10, command=security.destroy) # permet d'afficher un  bouton (il n'y a pas encore d'évènement associé)
    security_button.grid(row=4, column=1,columnspan = 2, pady=10)

    security.mainloop()  

if __name__ == "__main__":
    get_Logins()
    
    root = tk.Tk() 
    
    root.title("Knife detector")
    root.lift()
    root.resizable(False, False)

    App(root)