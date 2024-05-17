def multiplier_nombres_flotants(a, b):
    resultat = a * b
    return resultat

def normaliser_resultat(resultat):
    # Normalise pour avoir un seul chiffre à gauche de la virgule
    resultat_normalise = resultat / (10 ** (len(str(int(resultat))) - 1))
    return resultat_normalise

# Exemple d'utilisation
nombre_1 = float(input("Entrez le premier nombre en virgule flottante : "))
nombre_2 = float(input("Entrez le deuxième nombre en virgule flottante : "))

resultat = multiplier_nombres_flotants(nombre_1, nombre_2)
resultat_normalise = normaliser_resultat(resultat)

print(f"Le résultat normalisé de la multiplication est : {resultat_normalise}")
