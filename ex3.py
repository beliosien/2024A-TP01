# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
g = 9.8

distance = (speed**2 * math.sin(2 * math.radians(angle)))/g
str_afficher = f"Distance parcourue: {round(distance,2)}m"
print(str_afficher)

