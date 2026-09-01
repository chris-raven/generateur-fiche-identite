nom = input("Nom ?")
prenom = input("Prenom ?")
grade = input("Grade ?")
affectation = input("Voulez vous une affectation ?")

if affectation == "oui":
    print(f"bienvenue {grade} {nom} vous êtes affecté a la 11 CDI")

elif affectation == "non":
    print(f"Attention {grade} {nom} sans affectation vous n'aurez aucun bonus")

elif affectation == "pas sur":
    print(f" {grade} {nom} vous avez jusqu'a minuit pour choisir")

else:
    print(f" {grade} {nom} sans affectation vous n'aurez pas accès aux avantages")