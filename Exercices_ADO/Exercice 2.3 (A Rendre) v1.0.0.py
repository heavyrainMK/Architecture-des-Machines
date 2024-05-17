def conv_nombre_en_chiffre_romain(nombre_ou_romain):
    if type(nombre_ou_romain) == int:
        if not (0 < nombre_ou_romain < 4000):
            raise ValueError("Le nombre doit être compris entre 1 et 3999 inclus.")

        valeurs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chiffres_romains = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        resultat = ''
        for valeur, chiffre_romain in zip(valeurs, chiffres_romains):
            while nombre_ou_romain >= valeur:
                resultat += chiffre_romain
                nombre_ou_romain -= valeur

        return resultat
    elif type(nombre_ou_romain) == str:
        chiffres_romains = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
        total = 0
        prev_value = 0
        for chiffre_romain in nombre_ou_romain:
            valeur = chiffres_romains[chiffre_romain]
            if valeur > prev_value:
                total += valeur - 2 * prev_value
            else:
                total += valeur
            prev_value = valeur
        
        return total
    else:
        raise ValueError("L'entrée doit être soit un nombre entier, soit une chaîne de caractères représentant un chiffre romain.")

# Saisie de l'entrée par l'utilisateur avec gestion des erreurs
try:
    saisie_utilisateur = input("Entrez un nombre ou un chiffre romain : ")
    if saisie_utilisateur.isdigit():
        saisie_utilisateur = int(saisie_utilisateur)
except ValueError:
    pass

# Conversion et affichage
if type(saisie_utilisateur) == int:
    romain_resultat = conv_nombre_en_chiffre_romain(saisie_utilisateur)
    print(f"Le nombre {saisie_utilisateur} en chiffres romains est : {romain_resultat}")
elif type(saisie_utilisateur) == str:
    nombre_resultat = conv_nombre_en_chiffre_romain(saisie_utilisateur)
    print(f"Le chiffre romain {saisie_utilisateur} en nombre est : {nombre_resultat}")
else:
    print("Erreur : Veuillez entrer un nombre entier ou un chiffre romain.")