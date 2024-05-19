def PGCD(a,b, l={}):
    def get_k(a,b,r):
        s=0
        while a!=(b*s+r):
            s += 1
        return s

    if a%b == 0:
        return l
    else:
        l[a%b] = [(a,1),(b,-get_k(a,b,a%b))]
        return PGCD(b,a%b,l)

def coef_bezout(a,b):
    def elt_etranger_in_egalite(a,b,s):
        retour = False
        for elt in s:
            #print(elt[0])
            if (elt[0] != a) and (elt[0] != b):
                retour = True
        return retour
    
    def mult(old):
        coef = old[1]
        new = descent[s[i][0]]
        return [(new[0][0],new[0][1]*coef),(new[1][0],new[1][1]*coef)]

    def somme(l):
        submit = [0,0]
        for elt in l:
            if elt[0] == a:
                submit[0] = submit[0]+elt[1]
            if elt[0] == b:
                submit[1] = submit[1]+elt[1]

        print(f"L'égalité de Bezout : {a} ⨯ {submit[0]} + {b} ⨯ {submit[1]} = {gcd}")
        return submit

    descent = PGCD(a,b)
    gcd = min(descent.keys())
    s=[(gcd,1)]
    
    while elt_etranger_in_egalite(a,b,s):
        for i in range(len(s)):
            if (s[i][0] != a) or (s[i][0] != b):
                if s[i][0] in descent:
                    add = mult(s[i]) #descent[s[i][0]]
                    s.pop(i)
                    s.append(add[0])
                    s.append(add[1])

    return somme(s)

        
            
            
            


gcd = coef_bezout(537,123)
print(gcd)