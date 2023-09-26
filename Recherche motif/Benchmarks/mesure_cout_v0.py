import time
from boyer_moore import moore
from naif import naif

# Programme mesurant les coûts temporels des algorithmes de recherche
# d'un motif dans un texte
# Source du texte: http://www.crdp-strasbourg.fr/je_lis_libre/livres/Homere_Iliade.pdf
for i in range(1, 11):
    fichier = open("Textes/texte-{}.txt".format(i), "r")
    liste = fichier.readlines()
    t = "".join(liste)
    d_m, d_n = time.time(), time.time()
    m = "dieu"
    # Boyer-Moore
    moore(t, m)
    f_m = time.time()
    # Algorithme naif
    naif(t, m)
    f_n = time.time()
    # Affichage des résultats
    print("Algorithme de Boyer-Moore: ", f_m-d_m, "secondes.")
    print("Algorithme naif: ", f_n-d_n, "secondes.")
    fichier.close()
