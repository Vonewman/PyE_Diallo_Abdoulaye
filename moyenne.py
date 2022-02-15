def calcul_moyenne(notes):
    """Calcul la moyenne des notes

    Args:
        notes (string): les notes qui avec les matieres separees par '#'

    Returns:
       float: retourne un floattant de type float. Ex: 12.5
    """
    val = notes.split("#")
    val0 = val[0]
    nb = len(val)
    moyenneEtudiant = 0
    for i in range(nb):
        note = str(val[i])
        note = note.replace("]", "")
        note = note.split("[")
        notes = note[1]
        if ":" in notes:
            notes = notes.split(":")
            noteExamen = int(notes[-1])
            devoirs = notes[0]
            devoir_split = devoirs.split(";")
            n = len(devoir_split)
            notesDevoir = devoir_split[:n]
            moyenneMatiere: float
            moyDev = 0
            for j in range(n):
                moyDev = moyDev + float(notesDevoir[j])
            moyDev = float(moyDev/n)
            moyenneMatiere = ((moyDev + (2 * noteExamen)) / 3)
            moyenneEtudiant = float(moyenneEtudiant + moyenneMatiere)
        else:
            devoirs = notes[0]
            devoir_split = devoirs.split(";")
            n = len(devoir_split)
            notesDevoir = devoir_split[:n]
            moyenneMatiere: float
            moyDev = 0
            for j in range(n):
                moyDev = moyDev + float(notesDevoir[j])
            moyDev = float(moyDev/n)
            moyenneMatiere = moyDev
            moyenneEtudiant = float(moyenneEtudiant + moyenneMatiere)
            
    moyenneEtudiant = float(moyenneEtudiant / nb)
        
    return round(moyenneEtudiant, 2)

