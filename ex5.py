# TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.


def check_chaine(chaine):
    valid_char = {
        "G": 0,
        "B": 0,
        "S": 0
    }
    for c in chaine:
        if c not in valid_char.keys():
            return None
        else:
            valid_char[c] += 1
    return valid_char


country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
valid = check_chaine(code_medals)

Or = valid["G"] if valid else 0
Argent = valid["S"] if valid else 0
Bronze = valid["B"] if valid else 0

if sum([Or, Argent, Bronze]) == 0:
    print("Ceci est une chaine invalide.")
else:
    expected = f"{country}:\n- {Or} Or\n- {Argent} Argent\n- {Bronze} Bronze"
    print(expected)
