nom = input("Quel est ton nom ? ").capitalize()
prenom = input("Quel est ton prénom ? ").capitalize()

try:
    age = int(input("Quel est ton âge ? "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide pour l'âge.")
    exit()

sexe = input("Sexe (M/F) ? ").upper()

# Détermination du statut et du libellé du sexe
majeur_mineur = "Majeur(e)" if age >= 18 else "Mineur(e)"
genre = "Masculin" if sexe == "M" else "Féminin" if sexe == "F" else "Non spécifié"

# Affichage de la carte
print("\n" + "="*30)
print("      FICHE D'IDENTITÉ")
print("="*30)
print(f"Nom : {nom}")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans ({majeur_mineur})")
print(f"Sexe : {genre}")
print("="*30)
