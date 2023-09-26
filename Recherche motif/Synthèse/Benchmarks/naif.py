# Programme permettant de calculer le temps d'une recherche d'un motif dans un texte
def naif(texte, motif):
    """Programme permettant de calculer le temps d'une recherche d'un motif dans un texte.

    Arguments:
        - (str) motif: motif à rechercher
        - (str) texte: texte
    """
    cpt = 0
    for i in range(len(texte)-len(motif)+1):
        if texte[i:len(motif)+i] == motif:
            cpt += 1
    return cpt

def _test():
    """Fonction de test de l'algorithme naif."""
    assert naif("Le singe mange des bananes", "banane") == 1
    assert naif("Ceci est une phrase", "es") == 1
    assert naif("Les promesses n'engagent que ceux qui les ecoutent. Henri Queuille", "es") == 4

if __name__ == '__main__':
    _test()
