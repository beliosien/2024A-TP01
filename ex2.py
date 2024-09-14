# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math


def calculer_filtre(water_quantiy):
    return math.ceil((water_quantiy * 1) / 5)


def calculer_lampe(water_quantiy):
    return math.ceil((water_quantiy * 3) / 5)


def calculer_chlore(water_quantiy):
    return (water_quantiy * 0.5) / 5


def calculer_equipement(water_quantity):
    filtre = calculer_filtre(water_quantity)
    lampe = calculer_lampe(water_quantity)
    chlore = calculer_chlore(water_quantity)

    return filtre, lampe, chlore


water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
n_filter, n_light, kg_chlorine = calculer_equipement(water_quantity)

chaine_afficher = f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {n_filter}
\t- Lampe(s) UV : {n_light}
\t- Chlore : {kg_chlorine}kg"""

print(chaine_afficher)
