import pygame, sys
from pygame.locals import *
from pygame import * 

pygame.init()
mafenetre=display.set_mode((900,250))
display.set_caption('Number counter')
fond = Surface((900,250))
fond = fond.convert()
fond.fill((121,126,246))
""" Création d'un rectangle avec ses options, dans l'ordre :
    - l'objet auquee il est rattaché,
    - sa couleur (en RVB),
    - un tuple de 4 nombres
        * Coordonnées de son coin supérieur gauche
        * sa largeur et sa hauteur
    - un nombre indiquant l'épaisseur de son pourtour (mettre 0 s'il est rempli) """
def numeration(n):
    """
    """
    #-------------- Partie Romain --------------#
    global coords_x
    global coords_y
    coords_x=0 # Inisialisation des coordonnées de x a 0
    coords_y=0 # Inisialisation des coordonnées de y a 0

    def centaine():
        """Dessine le bloc des centaines
        sortie: dessin graphique"""
        for x in range(10): # Parcours des coordonnées de x 
            for y in range(0,10): # Parcours des coordonnées de y
                draw.rect(fond , (0, 50, 255), (1+24*x ,1+24*y ,24 ,24), 0) # Dessine l'Interieur rouge du carré
                draw.rect(fond , (0,0,0), (0+24*x ,0+24*y ,25 ,25), 1) # Dessine le Contour noir du carré

    def dizaine():
        """Dessine le bloc des dizaines
        sortie: dessin graphique"""
        
        if len(n)==3: # On verifie si le nombre passé en argument possède 3 chiffres (présence de centaine)
            coords_y=300 # On definie les coordonnées de y a 300
        elif len(n)==2: # On verifie si le nombre passé en argument possède 2 chiffres (non présence de centaine)
            coords_y=0 # On definie les coordonnées de y a 0

        for x in range(10):
            draw.rect(fond , (0, 127, 255), (coords_y+50*u,1+24*x,24 ,24), 0) # Dessine l'Interieur rouge du carré
            draw.rect(fond , (0,0,0), (coords_y+50*u,0+24*x ,25 ,25), 1) # Dessine le Contour noir du carré

    def unité():
        """Dessine le bloc des unités
        sortie: dessin graphique
        """
        
        if len(n)==1: # On verifie si le nombre passé en argument possède 1 chiffre (présence que d'unité)
            coords_y=0 # On definie les coordonnées de y a 0
        elif len(n)==2: # On verifie si le nombre passé en argument possède 2 chiffres (présence de dizaines)
            nb_diz=int(n[0]) # On recupère le chiffre de dizaine présent dans le nombre
            coords_y=25+50*nb_diz # On applique les coordonnées de x en fonction du nombre de dizaine
        elif len(n)==3: # On verifie si le nombre passé en argument possède 3 chiffres (présence de tout)
            nb_diz=int(n[1]) # On recupère le chiffre de dizaine présent dans le nombre
            coords_y=325+50*nb_diz # On applique les coordonnées de x en fonction du nombre de dizaine et des centaines

        # Permet de dessiner un carreau d'unité 
        for x in range(unite): # Parcours les chiffres de 0 au nombre d'unité
            draw.rect(fond , (0, 199, 255), (coords_y,coords_x+27*x ,24 ,24), 0) # Dessine l'Interieur rouge du carré
            draw.rect(fond , (0,0,0), (coords_y,coords_x+27*x ,25 ,25), 1) # Dessine le Contour noir du carré
    #-------------- Partie Romain --------------#


    #-------------- Partie Eliott --------------#
    for i in n:
        """Savoir si le nombre est une centaine, dizaine ou unité"""
        centaines=0 # On initialise le nombre de centaine a 0
        dizaines=0 # On initialise le nombre de dizaine a 0
        unite=0 # On initialise le nombre d'unité a 0
        if len(n) == 3:
            centaines=int(n[0]) 
            dizaines=int(n[1])
            unite=int(n[2])
        elif len(n) == 2:
            dizaines=int(n[0])
            unite=int(n[1])
        elif len(n) == 1:
            unite=int(n[0])
        

    for c in range(0,centaines): # On effectue le dessin en fonction du nombre de centaine
        centaine() # On appelle la fonction centaine
    
    for d in range(0,dizaines): # On effectue le dessin en fonction du nombre de dizaine
        u=d # On definie les coordonnées en fonction de la centaine (présente ou non)
        dizaine() # On appelle la fonction dizaine
    
    for u in range(0,unite):  # On effectue le dessin en fonction du nombre de dizaine
        unité() # On appelle la fonction unité
    #-------------- Partie Eliott --------------#


numeration("112")
# numeration("109")
# numeration("100")
# numeration("99")
# numeration("90")
# numeration("9")


mafenetre.blit(fond, (0, 0))
while True:
    display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()