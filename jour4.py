age = int(input("Quel âge as-tu ? "))
carte = input("As-tu une carte ? oui/non : ")
autorisation = input("As-tu une autorisation spéciale ? oui/non : ")

if (age >= 18 and carte == "oui") or autorisation == "oui":
    print("Accès autorisé")
else:
    print("Accès refusé")