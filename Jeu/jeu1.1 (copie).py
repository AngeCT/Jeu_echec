import pygame
import sys
import os
from pygame.locals import*

pygame.init()

#paramètres de la fenetre
ecran_info = pygame.display.Info()
ecran_largeur = ecran_info.current_w
ecran_hauteur = ecran_info.current_h
if ecran_largeur<ecran_hauteur:
    taille_case = ecran_largeur//8
else:
    taille_case = ecran_hauteur//8

largeur_fenetre = ecran_largeur
hauteur_fenetre = ecran_hauteur

# Définir la position initiale de la fenêtre (par exemple, 0 pixels à droite et 0 pixels en bas)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{0},{0}"

# Couleurs
blanc = (142, 229, 238)
noir = (16, 78, 139)
couleur_fond = (0,0,0)
couleur_fond2 = (255,255,255)
theme = couleur_fond

# Initialisation de la fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), NOFRAME)
fenetre.fill(theme)

#adaptation des tailles des pieces
nouvelle_largeur = taille_case
nouvelle_hauteur = taille_case

# Initialisation position de chaque pièce avec des variables
RB = pygame.image.load("RB.png").convert_alpha()
RB = pygame.transform.scale(RB, (nouvelle_largeur, nouvelle_hauteur))
RB_x= 4*taille_case
RB_y= 7*taille_case

DB = pygame.image.load("DB.png").convert_alpha()
DB = pygame.transform.scale(DB, (nouvelle_largeur, nouvelle_hauteur))
DB_x= 3*taille_case
DB_y= 7*taille_case

TB = pygame.image.load("TB.png").convert_alpha()
TB = pygame.transform.scale(TB, (nouvelle_largeur, nouvelle_hauteur))
TB_x= 0
TB_y= 7*taille_case

TB2 = pygame.image.load("TB.png").convert_alpha()
TB2 = pygame.transform.scale(TB2, (nouvelle_largeur, nouvelle_hauteur))
TB2_x= 7*taille_case
TB2_y= 7*taille_case

FB = pygame.image.load("FB.png").convert_alpha()
FB = pygame.transform.scale(FB, (nouvelle_largeur, nouvelle_hauteur))
FB_x= 2*taille_case
FB_y= 7*taille_case

FB2 = pygame.image.load("FB.png").convert_alpha()
FB2 = pygame.transform.scale(FB2, (nouvelle_largeur, nouvelle_hauteur))
FB2_x= 5*taille_case
FB2_y= 7*taille_case

CB = pygame.image.load("CB.png").convert_alpha()
CB = pygame.transform.scale(CB, (nouvelle_largeur, nouvelle_hauteur))
CB_x= taille_case
CB_y= 7*taille_case

CB2 = pygame.image.load("CB.png").convert_alpha()
CB2 = pygame.transform.scale(CB2, (nouvelle_largeur, nouvelle_hauteur))
CB2_x= 6*taille_case
CB2_y= 7*taille_case

PB1 = pygame.image.load("PB.png").convert_alpha()
PB1 = pygame.transform.scale(PB1, (nouvelle_largeur, nouvelle_hauteur))
PB1_x= 0
PB1_y= 6*taille_case

PB2 = pygame.image.load("PB.png").convert_alpha()
PB2 = pygame.transform.scale(PB2, (nouvelle_largeur, nouvelle_hauteur))
PB2_x =taille_case
PB2_y= 6*taille_case

PB3 = pygame.image.load("PB.png").convert_alpha()
PB3 = pygame.transform.scale(PB3, (nouvelle_largeur, nouvelle_hauteur))
PB3_x= 2*taille_case
PB3_y= 6*taille_case

PB4 = pygame.image.load("PB.png").convert_alpha()
PB4 = pygame.transform.scale(PB4, (nouvelle_largeur, nouvelle_hauteur))
PB4_x= 3*taille_case
PB4_y= 6*taille_case

PB5 = pygame.image.load("PB.png").convert_alpha()
PB5 = pygame.transform.scale(PB5, (nouvelle_largeur, nouvelle_hauteur))
PB5_x= 4*taille_case
PB5_y= 6*taille_case

PB6 = pygame.image.load("PB.png").convert_alpha()
PB6 = pygame.transform.scale(PB6, (nouvelle_largeur, nouvelle_hauteur))
PB6_x= 5*taille_case
PB6_y= 6*taille_case

PB7 = pygame.image.load("PB.png").convert_alpha()
PB7 = pygame.transform.scale(PB7, (nouvelle_largeur, nouvelle_hauteur))
PB7_x= 6*taille_case
PB7_y= 6*taille_case

PB8 = pygame.image.load("PB.png").convert_alpha()
PB8 = pygame.transform.scale(PB8, (nouvelle_largeur, nouvelle_hauteur))
PB8_x= 7*taille_case
PB8_y= 6*taille_case


#piece noire
RN = pygame.image.load("RN.png").convert_alpha()
RN = pygame.transform.scale(RN, (nouvelle_largeur, nouvelle_hauteur))
RN_x= 4*taille_case
RN_y= 0

DN = pygame.image.load("DN.png").convert_alpha()
DN = pygame.transform.scale(DN, (nouvelle_largeur, nouvelle_hauteur))
DN_x= 3*taille_case
DN_y =0

TN = pygame.image.load("TN.png").convert_alpha()
TN = pygame.transform.scale(TN, (nouvelle_largeur, nouvelle_hauteur))
TN_x= 0
TN_y= 0

TN2 = pygame.image.load("TN.png").convert_alpha()
TN2 = pygame.transform.scale(TN2, (nouvelle_largeur, nouvelle_hauteur))
TN2_x= 7*taille_case
TN2_y= 0

FN = pygame.image.load("FN.png").convert_alpha()
FN = pygame.transform.scale(FN, (nouvelle_largeur, nouvelle_hauteur))
FN_x= 2*taille_case
FN_y= 0

FN2 = pygame.image.load("FN.png").convert_alpha()
FN2 = pygame.transform.scale(FN2, (nouvelle_largeur, nouvelle_hauteur))
FN2_x= 5*taille_case
FN2_y= 0

CN = pygame.image.load("CN.png").convert_alpha()
CN = pygame.transform.scale(CN, (nouvelle_largeur, nouvelle_hauteur))
CN_x= taille_case
CN_y= 0

CN2 = pygame.image.load("CN.png").convert_alpha()
CN2 = pygame.transform.scale(CN2, (nouvelle_largeur, nouvelle_hauteur))
CN2_x= 6*taille_case
CN2_y= 0

PN1 = pygame.image.load("PN.png").convert_alpha()
PN1 = pygame.transform.scale(PN1, (nouvelle_largeur, nouvelle_hauteur))
PN1_x= 0
PN1_y= taille_case

PN2 = pygame.image.load("PN.png").convert_alpha()
PN2 = pygame.transform.scale(PN2, (nouvelle_largeur, nouvelle_hauteur))
PN2_x= taille_case
PN2_y= taille_case

PN3 = pygame.image.load("PN.png").convert_alpha()
PN3 = pygame.transform.scale(PN3, (nouvelle_largeur, nouvelle_hauteur))
PN3_x= 2*taille_case
PN3_y= taille_case

PN4 = pygame.image.load("PN.png").convert_alpha()
PN4 = pygame.transform.scale(PN4, (nouvelle_largeur, nouvelle_hauteur))
PN4_x= 3*taille_case
PN4_y= taille_case

PN5 = pygame.image.load("PN.png").convert_alpha()
PN5 = pygame.transform.scale(PN5, (nouvelle_largeur, nouvelle_hauteur))
PN5_x= 4*taille_case
PN5_y= taille_case

PN6 = pygame.image.load("PN.png").convert_alpha()
PN6 = pygame.transform.scale(PN6, (nouvelle_largeur, nouvelle_hauteur))
PN6_x= 5*taille_case
PN6_y= taille_case

PN7 = pygame.image.load("PN.png").convert_alpha()
PN7 = pygame.transform.scale(PN7, (nouvelle_largeur, nouvelle_hauteur))
PN7_x=taille_case*6
PN7_y=taille_case

PN8 = pygame.image.load("PN.png").convert_alpha()
PN8 = pygame.transform.scale(PN8, (nouvelle_largeur, nouvelle_hauteur))
PN8_x=taille_case*7
PN8_y=taille_case


# creation du tableau avec les infos des pieces
pieces = [
    ("RB", RB_x, RB_y), ("DB", DB_x, DB_y), ("TB", TB_x, TB_y),
    ("TB2", TB2_x, TB2_y), ("CB", CB_x, CB_y), ("CB2", CB2_x, CB2_y),
    ("FB", FB_x, FB_y), ("FB2", FB2_x, FB2_y), ("PB1", PB1_x, PB1_y),
    ("PB2", PB2_x, PB2_y), ("PB3", PB3_x, PB3_y), ("PB4", PB4_x, PB4_y),
    ("PB5", PB5_x, PB5_y), ("PB6", PB6_x, PB6_y), ("PB7", PB7_x, PB7_y),
    ("PB8", PB8_x, PB8_y), ("RN", RN_x, RN_y), ("DN", DN_x, DN_y),
    ("TN", TN_x, TN_y), ("TN2", TN2_x, TN2_y), ("CN", CN_x, CN_y),
    ("CN2", CN2_x, CN2_y), ("FN", FN_x, FN_y), ("FN2", FN2_x, FN2_y),
    ("PN1", PN1_x, PN1_y), ("PN2", PN2_x, PN2_y), ("PN3", PN3_x, PN3_y),
    ("PN4", PN4_x, PN4_y), ("PN5", PN5_x, PN5_y), ("PN6", PN6_x, PN6_y),
    ("PN7", PN7_x, PN7_y), ("PN8", PN8_x, PN8_y)
                ]

def case_vide(coord_x, coord_y):
    for piece, piece_x, piece_y in pieces:
        if piece_x == coord_x and piece_y == coord_y:
            return False
    return True

def piece_menacer(tab,piece_selectionnee):
    p_menacer = []
    for k in range(len(tab)):
        if 'B' in piece_selectionnee and 'N' in tab[k]:
            p_menacer.append(tab[k])
        elif 'N' in piece_selectionnee and 'B' in tab[k]:
            p_menacer.append(tab[k])
    return p_menacer

def meme_couleur(piece1, piece2):
    if ('B' in piece1 and 'N' in piece2) or ('N' in piece1 and 'B' in piece2):
        return False
    return True

def piece_case(coord_x, coord_y):
    if case_vide(coord_x, coord_y) == False:
        for piece, piece_x, piece_y in pieces:
            if coord_x == piece_x and coord_y == piece_y:
                return piece
    return None

def tab_anti_saut(tab):
    indice_piece = None
    indice_obstacle_av = None
    indice_obstacle_ap = None
    for k in range(len(tab)): #Trouve l'indice de la piece
        if tab[k] == 2:
            indice_piece = k
    for i in range(indice_piece,-1,-1): #Trouve l'indice 1 le plus proche de 2 avant 2
        if tab[i] == 1 or tab[i] == 4:
            indice_obstacle_av = i
            break
    if indice_obstacle_av != None: # si l'indice existe il supprime la suite
        for a in range(len(tab)):
            if a < indice_obstacle_av:
                tab[a] = 3
    for t in range(indice_piece,len(tab)): #Trouve l'indice 1 le plus proche de 2 apres 2
        if tab[t] == 1 or tab[t] == 4:
            indice_obstacle_ap = t
            break
    if indice_obstacle_ap != None: # si l'indice existe il supprime la suite
        for t in range(indice_piece,len(tab)):
            if t > indice_obstacle_ap:
                tab[t] = 3
    return(tab)


# Couleur du cercle
couleur_cercle = (255, 0, 0)

def mouvement_legal(fenetre, couleur_cercle, taille_case, piece_selectionnee, colonne, ligne):
    positions_valides = []
    piece_obstruante = []
    tab_colonne = []
    tab_ligne = []
    tab_diago_hg = []
    tab_diago_hd = []
    tab_diago_bg = []
    tab_diago_bd = []
    if en_deplacement == True:
        for piece, piece_x, piece_y in pieces:
            if piece == piece_selectionnee:
                piece_colonne = piece_x // taille_case
                piece_ligne = piece_y // taille_case

        if 'T' in piece_selectionnee:  # Vérifie si la pièce est une tour
            for colonne in range(8):
                for ligne in range(8):
                    if colonne == piece_colonne:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            tab_colonne.append(0)
                        elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                            tab_colonne.append(2)
                        elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                            tab_colonne.append(4)
                        else:
                            tab_colonne.append(1)
    
                    if ligne == piece_ligne:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            tab_ligne.append(0)
                        elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                            tab_ligne.append(2)
                        elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                            tab_ligne.append(4)
                        else:
                            tab_ligne.append(1)
                            
            tab_c_propre = tab_anti_saut(tab_colonne)
            tab_l_propre = tab_anti_saut(tab_ligne)

            for colonne in range(8): #on parcours la ligne
                if tab_l_propre[colonne] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = (colonne * taille_case + taille_case // 2, piece_ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((colonne, piece_ligne))
                    
                if tab_l_propre[colonne] == 1: # Case occuper par une piece de couleur diff
                    rayon_cercle = taille_case//2
                    centre_cercle = (colonne * taille_case + taille_case // 2, piece_ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case(colonne*taille_case, piece_ligne*taille_case)
                    piece_obstruante.append((piece_qui_bloque,colonne,piece_ligne))
                    
            for ligne in range(8): #on parcours la colonne
                if tab_c_propre[ligne] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = (piece_colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne, ligne))
                    
                if tab_c_propre[ligne] == 1: # Case occuper par une piece de couleur diff
                    rayon_cercle = taille_case//2
                    centre_cercle = (piece_colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case(piece_colonne*taille_case, ligne*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne,ligne))
                
          
                        
        elif 'F' in piece_selectionnee:  # Vérifie si la pièce est un fou
            for colonne in range(8):
                for ligne in range(8):
                    for k in range(8):
                        if (colonne + k == piece_colonne and ligne - k == piece_ligne): #diagonale bas_gauche
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_bg.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_bg.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_bg.append(4)
                            else:
                                tab_diago_bg.append(1)
                        
                        if (colonne - k == piece_colonne and ligne - k == piece_ligne): #diagonale bas_droite
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_bd.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_bd.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_bd.append(4)
                            else:
                                tab_diago_bd.append(1)
                                
                        if (colonne - k == piece_colonne and ligne + k == piece_ligne): #diagonale haut_droite
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_hd.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_hd.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_hd.append(4)
                            else:
                                tab_diago_hd.append(1)
                                
                        if (colonne + k == piece_colonne and ligne + k == piece_ligne): #diagonale haut_gauche
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_hg.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_hg.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_hg.append(4)
                            else:
                                tab_diago_hg.append(1)


            tab_hd_propre = tab_anti_saut(tab_diago_hd)
            tab_bd_propre = tab_anti_saut(tab_diago_bd)
            tab_hg_inverser = tab_anti_saut(tab_diago_hg)
            tab_hg_propre = tab_hg_inverser[::-1]
            tab_bg_inverser = tab_anti_saut(tab_diago_bg)
            tab_bg_propre = tab_bg_inverser[::-1]
            
            for hd in range(len(tab_hd_propre)):
                if tab_hd_propre[hd] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne + hd) * taille_case + taille_case // 2, (piece_ligne - hd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne+hd, piece_ligne-hd))
                    
                if tab_hd_propre[hd] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne + hd) * taille_case + taille_case // 2, (piece_ligne - hd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne + hd)*taille_case, (piece_ligne - hd)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne+hd, piece_ligne-hd))
                    
            for bd in range(len(tab_bd_propre)):
                if tab_bd_propre[bd] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne + bd) * taille_case + taille_case // 2, (piece_ligne + bd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne+bd, piece_ligne+bd))
                    
                if tab_bd_propre[bd] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne + bd) * taille_case + taille_case // 2, (piece_ligne + bd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne + bd)*taille_case, (piece_ligne + bd)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne+bd, piece_ligne+bd))
                    
            for hg in range(len(tab_hg_propre)):
                if tab_hg_propre[hg] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne - hg) * taille_case + taille_case // 2, (piece_ligne - hg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne-hg, piece_ligne-hg))
                    
                if tab_hg_propre[hg] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne - hg) * taille_case + taille_case // 2, (piece_ligne - hg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne - hg)*taille_case, (piece_ligne - hg)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne-hg, piece_ligne-hg))
                    
            for bg in range(len(tab_bg_propre)):
                if tab_bg_propre[bg] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne - bg) * taille_case + taille_case // 2, (piece_ligne + bg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne-bg, piece_ligne+bg))
                    
                if tab_bg_propre[bg] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne - bg) * taille_case + taille_case // 2, (piece_ligne + bg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne - bg)*taille_case, (piece_ligne + bg)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne-bg, piece_ligne+bg))

                        
        elif 'D' in piece_selectionnee:  # Vérifie si la pièce est une dame
            for colonne in range(8):
                for ligne in range(8):
                    if colonne == piece_colonne:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            tab_colonne.append(0)
                        elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                            tab_colonne.append(2)
                        elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                            tab_colonne.append(4)
                        else:
                            tab_colonne.append(1)
    
                    if ligne == piece_ligne:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            tab_ligne.append(0)
                        elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                            tab_ligne.append(2)
                        elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                            tab_ligne.append(4)
                        else:
                            tab_ligne.append(1)
                    for k in range(8):
                        if (colonne + k == piece_colonne and ligne - k == piece_ligne): #diagonale bas_gauche
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_bg.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_bg.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_bg.append(4)
                            else:
                                tab_diago_bg.append(1)
                        
                        if (colonne - k == piece_colonne and ligne - k == piece_ligne): #diagonale bas_droite
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_bd.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_bd.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_bd.append(4)
                            else:
                                tab_diago_bd.append(1)
                                
                        if (colonne - k == piece_colonne and ligne + k == piece_ligne): #diagonale haut_droite
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_hd.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_hd.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_hd.append(4)
                            else:
                                tab_diago_hd.append(1)
                                
                        if (colonne + k == piece_colonne and ligne + k == piece_ligne): #diagonale haut_gauche
                            if case_vide(colonne*taille_case, ligne*taille_case) == True:
                                tab_diago_hg.append(0)
                            elif piece_case(colonne*taille_case, ligne*taille_case) == piece_selectionnee:
                                tab_diago_hg.append(2)
                            elif meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee):
                                tab_diago_hg.append(4)
                            else:
                                tab_diago_hg.append(1)
                                
        
            tab_c_propre = tab_anti_saut(tab_colonne)
            tab_l_propre = tab_anti_saut(tab_ligne)
            tab_hd_propre = tab_anti_saut(tab_diago_hd)
            tab_bd_propre = tab_anti_saut(tab_diago_bd)
            tab_hg_inverser = tab_anti_saut(tab_diago_hg)
            tab_hg_propre = tab_hg_inverser[::-1]
            tab_bg_inverser = tab_anti_saut(tab_diago_bg)
            tab_bg_propre = tab_bg_inverser[::-1]


            for colonne in range(8): #on parcours la ligne
                if tab_l_propre[colonne] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = (colonne * taille_case + taille_case // 2, piece_ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((colonne, piece_ligne))
                    
                if tab_l_propre[colonne] == 1: # Case occuper par une piece de couleur diff
                    rayon_cercle = taille_case//2
                    centre_cercle = (colonne * taille_case + taille_case // 2, piece_ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case(colonne*taille_case, piece_ligne*taille_case)
                    piece_obstruante.append((piece_qui_bloque,colonne,piece_ligne))
                    
            for ligne in range(8): #on parcours la colonne
                if tab_c_propre[ligne] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = (piece_colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne, ligne))
                    
                if tab_c_propre[ligne] == 1: # Case occuper par une piece de couleur diff
                    rayon_cercle = taille_case//2
                    centre_cercle = (piece_colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case(piece_colonne*taille_case, ligne*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne,ligne))
                    
            
            for hd in range(len(tab_hd_propre)):
                if tab_hd_propre[hd] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne + hd) * taille_case + taille_case // 2, (piece_ligne - hd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne+hd, piece_ligne-hd))
                    
                if tab_hd_propre[hd] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne + hd) * taille_case + taille_case // 2, (piece_ligne - hd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne + hd)*taille_case, (piece_ligne - hd)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne+hd, piece_ligne-hd))
                    
            for bd in range(len(tab_bd_propre)):
                if tab_bd_propre[bd] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne + bd) * taille_case + taille_case // 2, (piece_ligne + bd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne+bd, piece_ligne+bd))
                    
                if tab_bd_propre[bd] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne + bd) * taille_case + taille_case // 2, (piece_ligne + bd) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne + bd)*taille_case, (piece_ligne + bd)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne+bd, piece_ligne+bd))
                    
            for hg in range(len(tab_hg_propre)):
                if tab_hg_propre[hg] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne - hg) * taille_case + taille_case // 2, (piece_ligne - hg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne-hg, piece_ligne-hg))
                    
                if tab_hg_propre[hg] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne - hg) * taille_case + taille_case // 2, (piece_ligne - hg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne - hg)*taille_case, (piece_ligne - hg)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne-hg, piece_ligne-hg))
                    
            for bg in range(len(tab_bg_propre)):
                if tab_bg_propre[bg] == 0: # Case vide possible
                    rayon_cercle = 10
                    centre_cercle = ((piece_colonne - bg) * taille_case + taille_case // 2, (piece_ligne + bg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    positions_valides.append((piece_colonne-bg, piece_ligne+bg))
                    
                if tab_bg_propre[bg] == 1: # Case vide possible
                    rayon_cercle = taille_case//2
                    centre_cercle = ((piece_colonne - bg) * taille_case + taille_case // 2, (piece_ligne + bg) * taille_case + taille_case // 2)
                    # Dessiner le cercle
                    pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                    piece_qui_bloque = piece_case((piece_colonne - bg)*taille_case, (piece_ligne + bg)*taille_case)
                    piece_obstruante.append((piece_qui_bloque,piece_colonne-bg, piece_ligne+bg))
                    

               
        elif 'R' in piece_selectionnee:  # Vérifie si la pièce est un roi
            for colonne in range(8):
                for ligne in range(8):
                    if colonne-1 <= piece_colonne <= colonne+1 and ligne-1 <= piece_ligne <= ligne+1:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            rayon_cercle = 10
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            positions_valides.append((colonne, ligne))
                            # Dessiner le cercle
                            pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                        else:
                            rayon_cercle = taille_case//2
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            piece_test=piece_case(colonne*taille_case, ligne*taille_case)
                            if meme_couleur(piece_selectionnee,piece_test) == False:
                                piece_obstruante.append((piece_test,colonne,ligne))
                                # Dessiner le cercle
                                pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                        
        elif 'PB' in piece_selectionnee:  # Vérifie si la pièce est un pion blanc
            for colonne in range(8):
                for ligne in range(8):
                    if (piece_ligne == ligne+1 or (piece_ligne==6 and piece_ligne == ligne+2)) and colonne == piece_colonne:
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            rayon_cercle = 10
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            positions_valides.append((colonne, ligne))
                            # Dessiner le cercle
                            pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                    if (piece_ligne == ligne+1 and (piece_colonne == colonne + 1 or piece_colonne == colonne - 1)):
                        if case_vide(colonne*taille_case, ligne*taille_case) == False and meme_couleur(piece_case(colonne*taille_case, ligne*taille_case),piece_selectionnee) == False:
                            rayon_cercle = taille_case//2
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            # Dessiner le cercle
                            pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
                            piece_test=piece_case(colonne*taille_case, ligne*taille_case)
                            piece_obstruante.append((piece_test,colonne,ligne))
                        
        elif 'PN' in piece_selectionnee:  # Vérifie si la pièce est un pion noir
            for colonne in range(8):
                for ligne in range(8):
                    if (piece_ligne == ligne-1 or (piece_ligne==1 and piece_ligne == ligne-2)) and colonne == piece_colonne:
                        rayon_cercle = 10
                        centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                        positions_valides.append((colonne, ligne))
                        # Dessiner le cercle
                        pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                        
        elif 'C' in piece_selectionnee:  # Vérifie si la pièce est une dame
            for colonne in range(8):
                for ligne in range(8):
                    if (ligne == piece_ligne+2 or ligne == piece_ligne-2) and (colonne == piece_colonne+1 or colonne == piece_colonne-1) or (ligne == piece_ligne+1 or ligne == piece_ligne-1) and (colonne == piece_colonne+2 or colonne == piece_colonne-2):
                        if case_vide(colonne*taille_case, ligne*taille_case) == True:
                            rayon_cercle = 10
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            positions_valides.append((colonne, ligne))
                            # Dessiner le cercle
                            pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle)
                        else:
                            rayon_cercle = taille_case//2
                            centre_cercle = (colonne * taille_case + taille_case // 2, ligne * taille_case + taille_case // 2)
                            piece_test=piece_case(colonne*taille_case, ligne*taille_case)
                            if meme_couleur(piece_selectionnee,piece_test) == False:
                                piece_obstruante.append((piece_test,colonne,ligne))
                                # Dessiner le cercle
                                pygame.draw.circle(fenetre, couleur_cercle, centre_cercle, rayon_cercle, 5)
    return positions_valides, piece_obstruante

#Définir la police des coordonées
font = pygame.font.Font(None, 36)  # Utilise la police par défaut avec une taille de 36
font2 = pygame.font.Font(None, 20)

#initialisation des variables de la fenetres parametres
parametre_cliquee = False
largeur_para = 200
hauteur_para = 100
x_para = 20 + hauteur_para
y_para = ecran_largeur - largeur_para

zone_a_effacer = pygame.Surface((largeur_para, hauteur_para))

# mode de jeu initial
mode_de_jeu = True

# Variable pour suivre l'état de sélection de la pièce
case_selectionnee = None
piece_selectionnee = None
case_selectionnee2 = None
initial_piece_x = None
initial_piece_y = None
en_deplacement = False
deplacement_x, deplacement_y = 0, 0

colonne_selectionnee=None
ligne_selectionnee=None

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if bouton_fermer_rect.collidepoint(event.pos):
                print("Fermeture de la fenetre")
                pygame.quit()
                sys.exit()
                
            if bouton_parametre_rect.collidepoint(event.pos) and parametre_cliquee == False and event.button == 1:
                print("Bouton parametres cliqué")
                pygame.draw.rect(fenetre, (0, 0,255), (ecran_largeur - largeur_para-10,bouton_hauteur+20,largeur_para,hauteur_para))
                zone_a_effacer.fill(couleur_fond)
                fenetre.blit(zone_a_effacer, (x_para, y_para))
                parametre_cliquee = True
            if bouton_parametre_rect.collidepoint(event.pos) and parametre_cliquee == True and event.button == 3:
                print("Bouton parametres RE-cliqué")
                zone_a_effacer.fill(couleur_fond)
                fenetre.blit(zone_a_effacer, (x_para, y_para))
                parametre_cliquee = False
                
            if bouton_retour_rect.collidepoint(event.pos):
                print("Bouton retour cliqué")
                import menu_jeu

            if bouton_on_rect.collidepoint(event.pos): 
                print("Mode clique & clique activé")
                mode_de_jeu = True
                
            if bouton_off_rect.collidepoint(event.pos):
                print("Mode drag & drop activé")
                mode_de_jeu = False

# DESSINER L'ECHEQUIER ET LES COORDONEES
    for ligne in range(8):
        for colonne in range(8):
            couleur = blanc if (ligne + colonne) % 2 == 0 else noir
            pygame.draw.rect(fenetre, couleur, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))
            # coordonnées
            couleur_coord = noir if (ligne + colonne) % 2 == 0 else blanc
            text_colonne = font.render(chr(ord('a') + colonne), True, couleur_coord)
            text_ligne = font.render(str(8 - ligne), True, couleur_coord)
            if colonne == 0:
                fenetre.blit(text_ligne, (colonne * taille_case + 2, ligne * taille_case + 2, taille_case, taille_case))
            if ligne == 7:
                fenetre.blit(text_colonne, (colonne * taille_case + (4 * taille_case) // 5, ligne * taille_case + (3 * taille_case) // 4, taille_case, taille_case))

# DESSINER LES PIECES
    for piece, piece_x, piece_y in pieces:
        fenetre.blit(globals()[piece], (piece_x, piece_y))

    # Mettre en surbrillance la case sélectionnée
    if case_selectionnee:
        colonne, ligne = case_selectionnee
        pygame.draw.rect(fenetre, (0, 255, 0), (colonne * taille_case, ligne * taille_case, taille_case, taille_case), 3)
        if piece_selectionnee != None:
            mouvement_legal(fenetre, couleur_cercle, taille_case, piece_selectionnee, colonne_selectionnee, ligne_selectionnee)

# DESSINER LES BOUTONS
    bouton_hauteur = 3 * taille_case // 4
    bouton_largeur = 3 * taille_case // 4

    # dessiner le bouton retour
    bouton_retour_x = ecran_largeur - 3 * bouton_largeur - 30
    bouton_retour_y = 10
    bouton_retour_rect = pygame.Rect(bouton_retour_x, bouton_retour_y, bouton_largeur, bouton_hauteur)
    img_bouton_retour = pygame.image.load("bouton_retour.png").convert_alpha()
    img_bouton_retour = pygame.transform.scale(img_bouton_retour, (bouton_largeur, bouton_hauteur))
    fenetre.blit(img_bouton_retour, (bouton_retour_x, bouton_retour_y))

    # dessiner le bouton fermer
    bouton_fermer_x = ecran_largeur - bouton_largeur - 10
    bouton_fermer_y = 10
    bouton_fermer_rect = pygame.Rect(bouton_fermer_x, bouton_fermer_y, bouton_largeur, bouton_hauteur)
    img_bouton_fermer = pygame.image.load("bouton_fermer.png").convert_alpha()
    img_bouton_fermer = pygame.transform.scale(img_bouton_fermer, (bouton_largeur, bouton_hauteur))
    fenetre.blit(img_bouton_fermer, (bouton_fermer_x, bouton_fermer_y))
    
    # dessiner le bouton parametres
    bouton_parametre_x = ecran_largeur - 2 * bouton_largeur - 20
    bouton_parametre_y = 10
    bouton_parametre_rect = pygame.Rect(bouton_parametre_x, bouton_parametre_y, bouton_largeur, bouton_hauteur)
    img_bouton_parametre = pygame.image.load("bouton_parametre.png").convert_alpha()
    img_bouton_parametre = pygame.transform.scale(img_bouton_parametre, (bouton_largeur, bouton_hauteur))
    fenetre.blit(img_bouton_parametre, (bouton_parametre_x, bouton_parametre_y))
    
    bouton_largeur2 = 219//4
    bouton_hauteur2 = 104//4
    
    # dessiner le bouton off
    bouton_off_x = ecran_largeur - 5 * bouton_largeur - 20
    bouton_off_y = 100
    
    texte2 = "MODE DRAG & DROP"
    texte2_surface = font2.render(texte2,False, blanc)
    texte2_rect = texte2_surface.get_rect()
    texte2_rect = (bouton_off_x,bouton_off_y+30)
    fenetre.blit(texte2_surface, texte2_rect)
    
    bouton_off_rect = pygame.Rect(bouton_off_x, bouton_off_y, bouton_largeur2, bouton_hauteur2)
    img_bouton_off = pygame.image.load("bouton_off.png").convert_alpha()
    img_bouton_off = pygame.transform.scale(img_bouton_off, (bouton_largeur2, bouton_hauteur2))
    fenetre.blit(img_bouton_off, (bouton_off_x, bouton_off_y))
    
    # dessiner le bouton on et de la description de sa fonction
    bouton_on_x = ecran_largeur - 5 * bouton_largeur - 20
    bouton_on_y = 150
    
    texte = "MODE CLIQUE & CLIQUE"
    texte_surface = font2.render(texte, False, blanc)
    texte_rect = texte_surface.get_rect()
    texte_rect = (bouton_on_x,bouton_on_y+30)
    fenetre.blit(texte_surface, texte_rect)
    
    bouton_on_rect = pygame.Rect(bouton_on_x, bouton_on_y, bouton_largeur2, bouton_hauteur2)
    img_bouton_on = pygame.image.load("bouton_on.png").convert_alpha()
    img_bouton_on = pygame.transform.scale(img_bouton_on, (bouton_largeur2, bouton_hauteur2))
    fenetre.blit(img_bouton_on, (bouton_on_x, bouton_on_y))

    case_vide_dispo, case_occuper_couleur_opps = mouvement_legal(fenetre, couleur_cercle, taille_case, piece_selectionnee, colonne_selectionnee, ligne_selectionnee)

# BOUCLE DES DEUX MODES DE JEU
    if mode_de_jeu == False: # 1er mode de deplacement : drag & drop
                # Si un clic de souris est détecté
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pos_souris = pygame.mouse.get_pos()
                    if pos_souris[0] < 8*taille_case:
                        colonne_selectionnee = pos_souris[0] // taille_case
                        ligne_selectionnee = pos_souris[1] // taille_case
                        case_selectionnee = (colonne_selectionnee, ligne_selectionnee)
        
                        for piece, piece_x, piece_y in pieces:
                            if piece_x <= pos_souris[0] <= piece_x + taille_case and piece_y <= pos_souris[1] <= piece_y + taille_case:
                                piece_selectionnee = piece
                                # on stocke la position actuelle de la pièce
                                initial_piece_x = piece_x
                                initial_piece_y = piece_y
                                deplacement_x = pos_souris[0] - piece_x
                                deplacement_y = pos_souris[1] - piece_y
                                en_deplacement = True
                                break
                            
                        if piece_selectionnee is not None:
                            print(f"Pièce sélectionnée : {piece_selectionnee}")
                        
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1 and en_deplacement:
                        pos_souris = pygame.mouse.get_pos()
                        if pos_souris[0] < 8*taille_case:
                            nouvelle_colonne = pos_souris[0] // taille_case
                            nouvelle_ligne = pos_souris[1] // taille_case
                            nouvelle_piece_x = nouvelle_colonne * taille_case
                            nouvelle_piece_y = nouvelle_ligne * taille_case
                            pieces.remove((piece_selectionnee, initial_piece_x, initial_piece_y))
                            pieces.append((piece_selectionnee, nouvelle_piece_x, nouvelle_piece_y))
                            print(f"{piece_selectionnee} deplacer de {chr(ord('a') + colonne_selectionnee)}{str(8 - ligne_selectionnee)} à {chr(ord('a') + nouvelle_colonne)}{str(8 - nouvelle_ligne)}")
                            en_deplacement = False
                            case_selectionnee = None  # Réinitialisez la case sélectionnée après le déplacement
                elif event.type == MOUSEMOTION:
                    if en_deplacement:
                        pos_souris = pygame.mouse.get_pos()
                        piece_x = pos_souris[0] - deplacement_x
                        piece_y = pos_souris[1] - deplacement_y
                        fenetre.blit(globals()[piece_selectionnee], (piece_x, piece_y))
                        pygame.display.flip()
                
                
    else: # 2eme mode de deplacement : clique & clique
        # Si un clic de souris est détecté et qu'aucune piece se deplace
        if event.type == MOUSEBUTTONDOWN and en_deplacement == False:
            if event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                if pos_souris[0] < 8*taille_case:
                    colonne_selectionnee = pos_souris[0] // taille_case
                    ligne_selectionnee = pos_souris[1] // taille_case
                    case_selectionnee = (colonne_selectionnee, ligne_selectionnee)
                    #case_vide(colonne_selectionnee*taille_case, ligne_selectionnee*taille_case)
        
                    for piece, piece_x, piece_y in pieces:
                        # Vérifier si une pièce est cliquée
                        if piece_x <= pos_souris[0] <= piece_x + taille_case and piece_y <= pos_souris[1] <= piece_y + taille_case:
                            piece_selectionnee = piece
                            # Stocker la position initiale de la pièce
                            position_initiale_x =  piece_x
                            position_initiale_y = piece_y
                            mouvement_stockage = (piece_selectionnee,piece_x//taille_case,piece_y//taille_case)
                            print(f'ca a selectionnee {piece_selectionnee}' )
                            en_deplacement = True
                            
        if event.type == MOUSEBUTTONDOWN and en_deplacement == True:#si un clique est detecter et qu'une piece est stocker
            print('ca rentre dans le boucle avec en_deplacement')
            if event.button == 1:
                pos_souris = pygame.mouse.get_pos()
                if pos_souris[0] < 8*taille_case:
                    colonne_selectionnee2 = pos_souris[0] // taille_case
                    ligne_selectionnee2 = pos_souris[1] // taille_case
                    case_selectionnee2 = (colonne_selectionnee2, ligne_selectionnee2)
                    #case_vide(colonne_selectionnee2*taille_case, ligne_selectionnee2*taille_case)
                    
                    if case_vide(colonne_selectionnee2*taille_case, ligne_selectionnee2*taille_case) == True:
                        print('ca remet la piece sur une case vide')
                        nouvelle_colonne = pos_souris[0] // taille_case
                        nouvelle_ligne = pos_souris[1] // taille_case
                        if (nouvelle_colonne, nouvelle_ligne) in case_vide_dispo:
                            print(f"{piece_selectionnee} deplacer de {chr(ord('a') + position_initiale_x//taille_case)}{8-(position_initiale_y//taille_case)} à {chr(ord('a') + nouvelle_colonne)}{str(8 - nouvelle_ligne)}")
                            pieces.remove((piece_selectionnee, position_initiale_x, position_initiale_y))
                            pieces.append((piece_selectionnee, nouvelle_colonne * taille_case, nouvelle_ligne * taille_case))
                        en_deplacement = False
                        case_selectionnee = None
                        piece_selectionnee = None
                    
                    else:
                        print('ca passe par la case pleine')
                        for piece, piece_x, piece_y in pieces:
                            # Vérifier quelle pièce est cliquée
                            if piece_x <= pos_souris[0] <= piece_x + taille_case and piece_y <= pos_souris[1] <= piece_y + taille_case:
                                piece_selectionnee2 = piece
                                # Stocker la position initiale de la pièce
                                position2_initiale_x =  piece_x
                                position2_initiale_y = piece_y
                                print(f'ca trouve une piece {piece_selectionnee2}')
                                print(pieces)
                                print((piece_selectionnee2, position2_initiale_x, position2_initiale_y))
                                print(case_occuper_couleur_opps)
                                if (piece_selectionnee2,colonne_selectionnee2,ligne_selectionnee2) in case_occuper_couleur_opps:
                                    #on supprime la piece selectionnee en 2eme
                                    if (piece_selectionnee2,position2_initiale_x,position2_initiale_y) in pieces:
                                        pieces.remove((piece_selectionnee2, position2_initiale_x, position2_initiale_y))
                                        #on deplace la piece selectionnee en 1er
                                        print(f"{piece_selectionnee} deplacer de {chr(ord('a') + position_initiale_x//taille_case)}{8-(position_initiale_y//taille_case)} à {chr(ord('a') + nouvelle_colonne)}{str(8 - nouvelle_ligne)}")
                                        if (piece_selectionnee,initial_piece_x,initial_piece_y) in pieces:
                                            pieces.remove((piece_selectionnee, initial_piece_x, initial_piece_y))
                                            pieces.append((piece_selectionnee, nouvelle_colonne * taille_case, nouvelle_ligne * taille_case))
                                            en_deplacement = False
                                            case_selectionnee = None
                                            case_selectionnee2 = None
                                            piece_selectionnee = None
                                            piece_selectionnee2= None
# Mettre à jour l'affichage
    pygame.display.flip()
