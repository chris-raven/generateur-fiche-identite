nom = input(" Nom ? ")
prenom = input("Prenom ? ")
humeur = input("Comment vas-tu aujourd'hui ? ")

print(f"Bienvenue {nom} {prenom} !")

if humeur == "bien":
    print("Super, content de l'entendre")

elif humeur == "très bien":
    print("Trop cool")

elif humeur == "bof":
    print("Allez courage !")

elif humeur == "mal":
    print("Oh, j'espère que ça ira mieux !")

else:
    print("Je ne connais pas cette réponse !")
    