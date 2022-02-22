import csv

from fonctions_valide import (
    notes_valide,
    numero_valide, 
    prenom_valide, 
    nom_valide, 
    date_valide, 
    row_vide,
    classe_valide,
    notes_valide
)
from modifier_donnee_invalide import format_data
from moyenne import calcul_moyenne

print("#############################################################################")
print("#############################################################################")
print("               BIENVENU AU MENU PROJET PYTHON                                ")
print("#############################################################################")
print("#############################################################################")

filepath = "projet-python.csv"

# initializing the title and rows list
fields = []
data_valide = []
data_invalide = []

data = []     # all the data

numero_list = []

# reading csv file
with open(filepath, 'r') as csvreader:
    
    # creating a csv reaer object
    csvreader = csv.reader(csvreader)
    
    # extracting fields names through first row
    fields = next(csvreader)
    
    # extracting each row one by one
    for row in csvreader:
        row[4] = format_data(row[4])
        if row_vide(row) and numero_valide(row[1]) and nom_valide(row[2]) and prenom_valide(row[3]) \
            and date_valide(row[4]) and classe_valide(row[5]) and notes_valide(row[6]):
            data_valide.append(row)
        else:
            data_invalide.append(row)
        
        data.append(row)
        
        # get total number of rows
    print("Le nombre total de lignes: %d " % (csvreader.line_num))


print("\n")

# printing the field names
print("Les noms des colonnes sont: " + ", ".join(field for field in fields))

print("\n")


while True:
    fhand = input("Tapez 'V' pour les donnes valides et 'I' pour les donnees invalides: ")
    fhand = fhand.lower()
    if fhand == "V" or fhand == "I":
        break
    else:
        print("Tapez une lettre valide")
    
print("\n")

if fhand == 'V' or fhand == "v":
    print(data_valide)
elif fhand == 'I' or fhand == "i":
    print(data_invalide)

print("\n")


inf = input("Donnez le numero d'un eleve pour acceder aux informations le concernant: ")


for d in data:
    if d[1] == inf:
        numero_list.append(d)

print("\n")

print("Voici les informations concernant l'élève: ", inf)

for i in range(len(numero_list)):
    if inf == numero_list[i][1]:
        print("Son Prenom: ", numero_list[i][3])
        print("Son Nom: ", numero_list[i][2])
        print("Sa Date de Naissance: ", format_data(numero_list[i][4]))
        print("Sa classe: ", numero_list[i][5])
        print("Ses Notes: ", numero_list[i][6])
    else:
        print("Ce numero n'est pas dans le fichier CSV")


    
del data_valide[14]
del data_valide[2]
data_valide_sorted = [] 
for row in data_valide:
   notes_tuples = row, calcul_moyenne(row[6])
   data_valide_sorted.append(notes_tuples)

print("\n")   

while True:
    fpre = input("Tapez 'O' pour voir les 5 premiers ou 'N' pour sortir du programme: ")
    fpre = fpre.lower()
    if fpre == "O" or fpre == "N":
        break
    else:
        print("Tapez une lettre valide")

print("\n")

if fpre == "O" or fpre == "o":
    print("Les 5 premiers sont rangés comme suit: ")
    print("\n")
    data_valide_sorted.sort(key=lambda moyenne:moyenne[:][1], reverse=True)
    for x in data_valide_sorted[:5]:
        print("L'élève: ", x[0], " a pour moyenne ", x[1])
        print("\n")
elif fpre == "N" or fpre == "n":
    print("Merci!")