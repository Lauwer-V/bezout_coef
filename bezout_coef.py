# Fonction pour calculer le PGCD de deux nombres et les coefficients de Bézout intermédiaires
def pgcd_bezout(a, b, coefficients={}):
    # Fonction auxiliaire pour calculer le coefficient k tel que a = b*k + r
    def get_coeff(a, b, r):
        k = 0
        while a != (b * k + r):
            k += 1
        return k

    # Si a est divisible par b, renvoyer le dictionnaire des coefficients de Bézout
    if a % b == 0:
        return coefficients
    else:
        # Mettre à jour le dictionnaire des coefficients de Bézout
        coefficients[a % b] = [(a, 1), (b, -get_coeff(a, b, a % b))]
        # Appel récursif de la fonction pgcd_bezout avec les nouveaux arguments b et a % b
        return pgcd_bezout(b, a % b, coefficients)

# Fonction pour calculer les coefficients de Bézout de deux nombres
def bezout_coefficients(a, b):
    # Fonction auxiliaire pour vérifier si l'égalité de Bézout contient des éléments autres que a et b
    def has_other_elt(a, b, s):
        for elt in s:
            if elt[0] not in (a, b):
                return True
        return False

    # Fonction auxiliaire pour multiplier un coefficient de Bézout par un autre
    def mult_coeff(old):
        coeff = old[1]
        new_coeff = coefficients[s[i][0]]
        return [(new_coeff[0][0], new_coeff[0][1] * coeff),
                (new_coeff[1][0], new_coeff[1][1] * coeff)]

    # Fonction auxiliaire pour calculer la somme des coefficients de Bézout
    def sum_coeff(l):
        a_coeff, b_coeff = 0, 0
        for elt in l:
            if elt[0] == a:
                a_coeff += elt[1]
            elif elt[0] == b:
                b_coeff += elt[1]
        print(f"L'égalité de Bezout : {a} ⨯ {a_coeff} + {b} ⨯ {b_coeff} = {gcd}")
        return a_coeff, b_coeff

    # Calculer le PGCD et les coefficients de Bézout intermédiaires
    coefficients = pgcd_bezout(a, b)
    # Récupérer le PGCD
    gcd = min(coefficients.keys())
    # Initialiser la liste des coefficients de Bézout
    s = [(gcd, 1)]

    # Tant que l'égalité de Bézout contient des éléments autres que a et b
    while has_other_elt(a, b, s):
        for i in range(len(s)):
            if s[i][0] not in (a, b) and s[i][0] in coefficients:
                add_coeff = mult_coeff(s[i])
                s.pop(i)
                s.append(add_coeff[0])
                s.append(add_coeff[1])

    # Calculer et renvoyer les coefficients de Bézout
    return sum_coeff(s)
