def chiffre_romain_en_nombre_decimal(chiffre_romain):
    chiffres_romains = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    decimal = 0

    i = 0
    while i < len(chiffre_romain):
        if (i < len(chiffre_romain) - 1) and (chiffres_romains[chiffre_romain[i]] < chiffres_romains[chiffre_romain[i + 1]]):
            decimal += chiffres_romains[chiffre_romain[i + 1]] - chiffres_romains[chiffre_romain[i]]
            i += 2
        else:
            decimal += chiffres_romains[chiffre_romain[i]]
            i += 1

    return decimal

def nombre_decimal_en_chiffre_romain(nombre_decimal):
    if not (0 < nombre_decimal < 4000):
        raise ValueError("Le nombre decimal doit être compris entre 1 et 3999 inclus.")
    
    valeurs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    chiffres_romains = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    resultat = ''
    for valeur, chiffre_romain in zip(valeurs, chiffres_romains):
        while nombre_decimal >= valeur:
            resultat += chiffre_romain
            nombre_decimal -= valeur

    return resultat

def additioner_chiffres_romains(chiffre1, chiffre2):
    resultat_decimal = chiffre_romain_en_nombre_decimal(chiffre1) + chiffre_romain_en_nombre_decimal(chiffre2)
    resultat_chiffres_romains = nombre_decimal_en_chiffre_romain(resultat_decimal)

    return resultat_chiffres_romains

def saisie_utilisateur():
    try:
        # Saisie de l'utilisateur
        saisie_utilisateur1 = int(input("Entrez le premier nombre : "))
        saisie_utilisateur2 = int(input("Entrez le deuxieme nombre : "))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers.")
        exit()

    # Convertit le saisie de l'utilisateur en chiffres romaines
    resultat_chiffres_romains_1 = nombre_decimal_en_chiffre_romain(saisie_utilisateur1)
    resultat_chiffres_romains_2 = nombre_decimal_en_chiffre_romain(saisie_utilisateur2)

    return resultat_chiffres_romains_1, resultat_chiffres_romains_2

# Le resultat du saisie de l'utilisateur
resultat_chiffres_romains_1, resultat_chiffres_romains_2 = saisie_utilisateur()

# Convertit des chiffres romaines en nombres decimaux, les additionnent, et reconvertit le resultat en chiffres romaines.
resultat_decimal = chiffre_romain_en_nombre_decimal(resultat_chiffres_romains_1) + chiffre_romain_en_nombre_decimal(resultat_chiffres_romains_2)
resultat_final = nombre_decimal_en_chiffre_romain(resultat_decimal)

# Affichage du resultat final
print(f"Le résultat de l'addition est : {resultat_final}")



