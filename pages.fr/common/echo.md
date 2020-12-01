# echo

> Affiche les paramètres donnés.

- Affiche un message (les guillemets sont facultatifs) :

`echo "{{Hello World}}"`

- Affiche un message avec des variables d'environment :

`echo "{{Ma variable PATH est $PATH}}"`

- Affiche un message sans une nouvelle ligne à la fin :

`echo -n "{{Hello World}}"`

- Ajoute un message à un fichier :

`echo "{{Hello World}}" >> {{fichier.txt}}`

- Active l'interprétation des spécificateurs d'échappement :

`echo -e "{{Colonne 1\tColonne 2}}"`
