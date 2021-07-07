# -*-coding:Utf-8 -*
print("hello")

# 1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
# “positif” ou “négatif”.

# Entier = int(input('Exercice 1 Entrez un nombre/chiffre : '))
#
# if Entier >= 0:
#     print("Positif")
# else:
#     print("Négatif")


# 2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
# négatif, et affiche ce résultat.

# Entier = int(input('Exercice 2 Entrez un nombre/chiffre : '))
#
# if Entier < 0:
#      print("Négatif")
# else:
#     if Entier !=0:
#         print("Positif")
#     else:
#         print("Nul")

# 3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
# prédéfinie évidemment).


# Reel = float(input('Exercice 3 Entrez un nombre/chiffre : '))
# if Reel > 0:
#     print("La valeur absolue est : ", Reel)
# else:
#     AbsReel = Reel*(-2)+Reel
#     print("La valeur absolue est : ", AbsReel)

# 4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
# à l’entier supérieur).

# Reel = float(input('Exercice 4 Entrez un nombre/chiffre : '))
# EntierReel = int(Reel)
# DecReel = Reel-EntierReel
# if DecReel > 0:
#     if DecReel < 0.5:
#         print("Arrondie à l'entier le plus proche (l'inférieur) : ", EntierReel)
#     else:
#         EntierReel = EntierReel + 1
#         print("Arrondie à l'entier le plus proche (Supérieur) : ", EntierReel)
# if DecReel < 0:
#     if DecReel < -0.5:
#         EntierReel = EntierReel - 1
#         print("Arrondie à l'entier le plus proche (l'inférieur) : ", EntierReel)
#     else:
#         print("Arrondie à l'entier le plus proche (Supérieur) : ", EntierReel)

# 5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
# compte des années bissextiles).

# NumJour=0
# NumMois = int(input('Exercice 5 Entrez un numéro de mois : '))
# while NumMois > 12:
#     print("entrez un numéro de mois entre 0 et 12")
#     NumMois = int(input('Numéro de mois entre 0 et 12 : '))
# if (NumMois in [1,3,5,7,8,10,12]):
#     NumJour = 31
#     print("le nombre de jour du mois", NumMois, "est : ", NumJour)
# elif NumMois ==2:
#     NumJour = 28
#     print("le nombre de jour du mois de février est : ", NumJour)
# else :
#     NumJour=30
#     print("le nombre de jour du mois", NumMois, "est : ", NumJour)


# 6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
# 4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
# (2000 était une année bissextile).

# NumAnnee = int(input("Exercice 6 Entrez un nombre d'année : "))
# if (NumAnnee%4 ==0) and (NumAnnee%100!=0):
#     print("Année bissextile tous les 4 ans")
# elif NumAnnee%400 == 0:
#     print("Année bissextile tous les 400 ans")
# else :
#     print("Année pas bissextile")


# 7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
# et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.


# Algorithme qui catégorise toutes les possibilités
# NumJour = int(input("Exercice 6 Entrez un nombre de jour : "))
# NumMois = int(input("Exercice 6 Entrez un nombre de mois : "))
#
# # Conditions pour l'hiver
# if NumMois in [1, 2]:
#     print("nous sommes en hiver en Janvier Février")
# elif NumJour > 20 and NumMois == 12:
#     print("nous sommes en hiver a partir du 21 Décembre")
# elif NumJour < 21 and NumMois == 3:
#     print("nous sommes en hiver avant le 21 Mars")
#
# # Conditions pour l'automne
# elif NumMois in [10, 11]:
#     print("nous sommes en automne en Octobre Novembre")
# elif NumJour > 20 and NumMois == 9:
#     print("nous sommes en automne partir du 21 Septembre")
# elif NumJour < 21 and NumMois == 12:
#     print("nous sommes en automne avant le 21 Décembre")
#
# # Conditions pour le Printemps
# elif NumMois in [4, 5]:
#     print("nous sommes en automne en Avril Mai")
# elif NumJour > 20 and NumMois == 3:
#     print("nous sommes au Printemps partir du 21 Mars")
# elif NumJour < 21 and NumMois == 6:
#     print("nous sommes au Printemps avant le 21 Juin")
# else:
#     print('nous sommes en été')

# TEST
# Algorithme qui assigne une valeur pour additionner les jours et les mois pour les comparer

NumJour = int(input("Exercice 6 Entrez un nombre de jour : "))
NumMois = int(input("Exercice 6 Entrez un nombre de mois : "))
NumMois = NumMois * 100
SommeJM = NumMois + NumJour
if 320 < SommeJM < 621:
    print('nous sommes au printemps')
elif 620 < SommeJM < 921:
    print('nous sommes en été')
elif 920 < SommeJM < 1221:
    print('nous sommes en automne')
else:
    print('nous sommes en hiver')
