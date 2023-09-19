# Julieta María Fonseca Nava 
# 03/09/23
# TP1 - Word_Count

# Séparer la phrase en une liste (mots) et compter les éléments
# Input: La phrase (string)
# Output: Nbr de mots (int)
def count_word(phrase):
    word_list = phrase.split(" ")
    word_lenght = len(word_list)
    return word_lenght
