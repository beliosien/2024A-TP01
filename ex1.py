# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ?")
date = input(" Date du record ?")
discipline = input(" Dans quelle discipline ?")
categorie = input(" Dans une catégorie spécifique ?")
record = input(" Quel est le record ? ")

chaine_a_afficher = f"\nNouveau Record:\n--------------------\n{date} - {discipline} - {categorie}:\n\t{athlete} ({country}) - {record}"
print(chaine_a_afficher)
