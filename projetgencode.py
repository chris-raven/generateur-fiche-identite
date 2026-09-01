import random
import string

print("--- GÉNÉRATEUR DE MOTS DE PASSE ---")

# 1. Demander la longueur
longueur = int(input("Combien de caractères veux-tu ? "))

# 2. Demander si on veut des chiffres et des symboles
avec_chiffres = input("Veux-tu des chiffres ? (oui/non) : ").lower()
avec_symboles = input("Veux-tu des symboles ? (oui/non) : ").lower()

# On commence par la base : les lettres (minuscules et majuscules)
caracteres = string.ascii_letters

# Si l'utilisateur répond "oui", on ajoute les chiffres
if avec_chiffres == "oui":
    caracteres += string.digits

# Si l'utilisateur répond "oui", on ajoute les symboles
if avec_symboles == "oui":
    caracteres += string.punctuation

# 3. Génération du mot de passe avec les caractères choisis
liste_aleatoire = random.choices(caracteres, k=longueur)
mot_de_passe = "".join(liste_aleatoire)

# 4. Affichage du résultat
print(f"Voici ton mot de passe sécurisé : {mot_de_passe}")