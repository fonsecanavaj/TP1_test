# Julieta María Fonseca Nava 
# 03/09/23
# TP1 - Word_Count


# Obtenir de l'utilisateur la phrase à compter 
message = input("Écrivez une phrase contenant seulement des mots en minuscules ainsi que des espaces.\n")


# Séparer la phrase en une liste (mots) et compter les éléments
# Input: Le message (string)
# Output: Nbr de mots (int)
def count_word(phrase):
    word_list = phrase.split(" ")
    word_lenght = len(word_list)
    return word_lenght


# Afficher le nombre exact de mots 
print(f"Le nombre de mots dans votre phrase est de {count_word(message)} mots.")
