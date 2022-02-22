def format_data(chaine):
    """Modifie le format des dates

    Args:
        chaine (string): une date de n'importe quel format

    Returns:
        string: return une date de format dd/mm/yyyy
    """
    chaine = chaine.strip()
    for x in chaine:
        if (x == ".") or (x == ",") or (x == ":") or \
            (x == " ") or (x == "_") or (x == "-") or (x == ";"):
                chaine = chaine.replace(x, "/")
    
    if chaine == "":
        chaine = "00/00/00"
    
    
    liste_chaine = chaine.split("/")
    
    
    if liste_chaine[1] in "Janvier" or liste_chaine[1] in "janvier":
        liste_chaine[1] = "01"
    if liste_chaine[1] in "Fevrier" or liste_chaine[1] in "fevrier":
        liste_chaine[1] = "02"
    if liste_chaine[1] in "Mars" or liste_chaine[1] in "mars":
        liste_chaine[1] = "03"
    if liste_chaine[1] in "Avril" or liste_chaine[1] in "avril":
        liste_chaine[1] = "04"
    if liste_chaine[1] in "Mai" or liste_chaine[1] in "mai":
        liste_chaine[1] = "05"
    if liste_chaine[1] in "Juin" or liste_chaine[1] in "juin":
        liste_chaine[1] = "06"
    if liste_chaine[1] in "Juillet" or liste_chaine[1] in "juillet":
        liste_chaine[1] = "07"
    if liste_chaine[1] in "Août" or liste_chaine[1] in "août":
        liste_chaine[1] = "08"
    if liste_chaine[1] in "Septembre" or liste_chaine[1] in "septembre":
        liste_chaine[1] = "09"
    if liste_chaine[1] in "Octobre" or liste_chaine[1] in "octobre":
        liste_chaine[1] = "10"
    if liste_chaine[1] in "Novembre" or liste_chaine[1] in "novembre":
        liste_chaine[1] = "11"
    if liste_chaine[1] in "Decembre" or liste_chaine[1] in "decembre":
        liste_chaine[1] = "12"
    
    if liste_chaine[2] == "99":
        liste_chaine[2] = "1999"
        
    
    chaine = "/".join(liste_chaine)
    
    return chaine
