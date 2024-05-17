def comparer_nombres_complement_2(nombre1, nombre2):
    # Bits de signe
    signe_bit1 = int(nombre1[0])
    signe_bit2 = int(nombre2[0])

    # Si les bits de signe sont différents, c’est le nombre où il vaut 0 qui est le plus grand
    if signe_bit1 != signe_bit2:  # Bits de signe différents
        if signe_bit1 == 0:  # Si le bit de signe du premier nombre est positif
            return f"{nombre1} est plus grand que {nombre2}" # Le premier nombre est plus grand que le deuxième nombre
        else:
            return f"{nombre2} est plus grand que {nombre1}" # Le deuxième nombre est plus grand que le premier nombre

    # Si les bits de signe sont les mêmes, alors on compare les valeurs absolues des nombres
    valeur_abs1 = int(nombre1[1:], 2)
    valeur_abs2 = int(nombre2[1:], 2)

    if valeur_abs1 > valeur_abs2: # Si la valeur absolue du premier nombre est plus grande que celle du deuxième nombre
        return f"{nombre1} est plus grand que {nombre2}" # Le premier nombre est plus grand que le deuxième nombre
    elif valeur_abs1 < valeur_abs2:
        return f"{nombre2} est plus grand que {nombre1}" # Le deuxième nombre est plus grand que le premier nombre
    else:
        return f"{nombre1} est égal à {nombre2}" # Les nombres sont égaux

# Saisie utilisateur des nombres en complément à 2
nombre1 = input("Premier nombre représenté en complément à 2 : ")
nombre2 = input("Deuxième nombre représenté en complément à 2 : ")

resultat = comparer_nombres_complement_2(nombre1, nombre2)
print(resultat)



