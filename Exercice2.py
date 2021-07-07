# -*-coding:Utf-8 -*
print("hello")
###################################################################################################
# Créer un nouveau fichier Exercice2.py dans votre projet et configurer le charset en utf-8
# En utilisant des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :
# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.

# NbEntPos = float(input("Entrez un entier positif : "))
# INTEGNbEntPos = int(NbEntPos)
#
# while NbEntPos != INTEGNbEntPos or NbEntPos < 0:
#     print("Veuillez entrer un nombre entier positif svp : ")
#     NbEntPos = float(input())
#     INTEGNbEntPos = int(NbEntPos)
# print("Félicitation vous avez un entier positif")

# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

# Mon programme

# liste10Ent = []
# for i in range(10):
#     liste10Ent.append(int(input("Entrez 10 entiers : ")))
# #n=0
# for n in range(10):
#     if liste10Ent[n] > 0:
#         print("Félicitation vous avez un entier positif")
#         # n = n + 1
#     elif liste10Ent[n] < 0:
#         print("entier négatif")
#         # n = n + 1
#     else:
#         print("entier nul")
#         # n = n + 1
#
# print("la boucle est finie")


# Programme du prof
# cpt=0
# for i in range(10):
#     a = int(float(input("Saisir un entier positif ou négatif")))
#     if a >=0:
#         cpt =cpt +1
# print("le nom d'entier positif saisi est", cpt)


# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.

# Somme = 0
# i = 0
# a = 0
# print("Saisir un entier positif ou négatif")
# while i < 10 and a >= 0:
#     a = int(float(input("entier numéro" + str(i+1))))
#     if a >= 0:
#         Somme = Somme + a
#         i = i + 1
# print("la somme est sans compter le nombre négatif : ", Somme)

# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.

# Somme = 0
# i = 0
# a = 0
# p =0 #nb de positif pour la moyenne
# print("Saisir un entier positif ou négatif")
# while i < 10 and a >= 0:
#     a = int(float(input()))
#     if a >= 0:
#         Somme = Somme + a
#         i = i + 1
#         p=p+1

#print("la somme est sans compter le nombre négatif : ", Somme)
#print("la moyenne es : ", Somme / p)


#dico = {'computer': 'ordinateur', 'keyboard': 'clavier', 'mouse': 'souris'}

s = [0]
for i in range(5):
    s[i] = s.append("bonjour")
    print(s)

