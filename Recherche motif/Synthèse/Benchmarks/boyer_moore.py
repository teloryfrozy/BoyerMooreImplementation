# Programme selon l'algorithme de recherche d'un motif de Boyer-Moore
def tbl_dcl(motif):
    """Renvoie le tableau de décalage du motif."""
    return [{motif[j]: j for j in range(i)} for i in range(len(motif)+1)]

def moore(texte, motif):
    """Renvoie le nombre d'occurrences de motif dans un texte.

    Arguments:
        - (str) texte: texte quelconque
        - (str) motif: motif à rechercher dans texte

    Algorithme:
        tbl_decalage: table de décalage du motif
        lng: longueur du motif
        nb_occ: 0
        i: 0
        Tant que i <= longueur de texte - lng
            dcl = 0
            Pour j allant de lng à 0
                Si motif[j] != texte[i+j]
                    Si texte[i+j] dans motif
                        dcl: dcl + j - tbl_decalage[j][texte[i+j]]
                    Sinon
                        i: i + lng
                    Arrêt de la boucle
                Sinon si dcl = 0
                    nb_occ: nb_occ + 1
                    dcl: 1
        Renvoyer nb_occ
    """
    tbl_decalage = tbl_dcl(motif)
    lng = len(motif)
    nb_occ = 0
    i = 0
    while i <= len(texte)-lng: # jusqu'à temps que lng soit supérieur à len(texte) - i <=> pas de motif possible
        dcl = 0 # valeur du décalage
        for j in range(len(motif)-1, -1, -1): # parcours du motif de la fin vers le début
            if motif[j] != texte[i+j]:
                if texte[i+j] in tbl_decalage[j]: # saut de la longueur associée
                    dcl += j - tbl_decalage[j][texte[i+j]]
                else: # saut de lng
                    dcl += lng
                break
        if dcl == 0: # occurence trouvée
            nb_occ += 1
            dcl = 1
        i += dcl
    return nb_occ

def _test():
    """Fonction de test de l'algorithme de Boyer Moore."""
    assert moore("Le singe mange des bananes", "banane") == 1
    assert moore("Ceci est une phrase", "es") == 1
    assert moore("Les promesses n'engagent que ceux qui les ecoutent. Henri Queuille", "es") == 4

if __name__ == '__main__':
    _test()
