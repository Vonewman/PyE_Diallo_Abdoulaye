# Ce fichier contient les fonctions
# qui verifient si les donnees sont valides

import re

def numero_valide(chaine):
    """Check pour voir si le numero est valide ou pas

    Args:
        chaine (string): un numero

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    # Expression reguliere qui valide la colonne numero
    # Composé de lettre majuscule et de chiffre
    # Sa taille est 7
    numero_re = r"[A-Z0-9]"
    if re.match(numero_re, chaine) and len(chaine) == 7:
        return True
    else:
        return False
    

def prenom_valide(chaine):
    """Check pour voir si le prenom est valide ou pas

    Args:
        chaine (string): un prenom

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    # Expression reguliere qui valide la colonne prenom
    # Commence par une lettre
    # Contient au moins 3 lettres
    prenom_re = r"^[A-Za-z]([A-Za-z]){2,}"
    if re.match(prenom_re, chaine) and len(chaine) >= 3:
        return True
    else:
        return False
    

def nom_valide(chaine):
    """Check pour voir si le nom est valide ou pas

    Args:
        chaine (string): un nom

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    # Expression reguliere qui valide la colonne prenom
    # Commence par une lettre
    # Contient au moins 2 lettres
    nom_re = r"^[A-Za-z]([A-Za-z]){1,}"
    if re.match(nom_re, chaine) and len(chaine) >= 2:
        return True
    else:
        return False
    
def date_valide(chaine):
    """Check pour voir si la date est valide ou pas

    Args:
        chaine (string): une date

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    # Format de date et transformer toutes les dates sous ce format
    # j'ai choisit le format dd/mm/yyyy
    date_re = r"^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"
    
    if re.match(date_re, chaine):
        return True
    else:
        return False
    
def row_vide(row):
    """Check pour voir si la ligne est valide ou pas

    Args:
        chaine (string): une ligne de caracteres

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    if row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[6] != '':
        return True
    else:
        return False
    
   

def classe_valide(chaine):
    """Check pour voir si la classe est valide ou pas

    Args:
        chaine (string): une classe. Ex: 6em A

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    # 6em à 3em plus les lettres A & B
    
    chaine = chaine.strip()  # cas: '    3em        A '
    
    c1 = r"^([3-6])([a-z]+)[ ]([A-B])$" # cas1: 3em A ou 3ieme A ou 3eme A
    c2 = r"^([3-6])([a-z]+)([A-B])$"    # cas2: 3emA ou 3iemeA ou 3emeA
    c3 = r"^([3-6])[ ]([a-z]+)[ ]([A-B])$" # cas3: 3 em A ou 3 ieme A ou 3 eme A
    c4 = r"^([3-6])([è])([a-z]+)([A-B])$"  # cas4: 3èmA ou 3ièmeA ou 3èmeA
    
       
    if re.match(c1, chaine) or re.match(c2, chaine) or re.match(c3, chaine) or re.match(c4, chaine):
        return True
    else:
        return False
    

def notes_valide(notes):
    """Check pour voir si les notes sont valides ou pas

    Args:
        chaine (string): une ligne de notes

    Returns:
        Boolean: retourne Vrai ou Faux
    """
    count_dieze = 0
    for x in notes:
        if x == "#":
            count_dieze += 1
    chaine = ""
    val = notes.split("#")
    val0 = val[0]
    nb = len(val)
    moyenneEtudiant = 0
    for i in range(nb):
        note = str(val[i])
        note = note.replace("]", "")
        note = note.split("[")
        notes = note[-1]
        chaine = chaine + notes
        
    
    if "," not in chaine and count_dieze == 5:
        return True
    else:
        return False
