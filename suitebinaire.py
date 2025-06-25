# Entrez votre programme ci-dessous
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

chaine_binaire = input("Saisir une chaîne de caractères représentant une suite binaire : ")

complement = ''
for bit in chaine_binaire:
    if bit == '0':
        complement += '1'
    else:
        complement += '0'

print(complement)
