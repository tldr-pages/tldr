# echo

> Affiche les paramètres donnés dans la console.
> Plus d'informations : <https://www.gnu.org/software/coreutils/echo>.

- Affiche un message (les guillemets sont facultatifs) :

`echo "{{Hello World}}"`

- Affiche un message avec des variables d'environnement :

`echo "{{Ma variable PATH est $PATH}}"`

- Affiche un message sans retour à la ligne :

`echo -n "{{Hello World}}"`

- Ajoute un message à un fichier :

`echo "{{Hello World}}" >> {{fichier.txt}}`

- Active l'interprétation des spécificateurs d'échappement :

`echo -e "{{Colonne 1\tColonne 2}}"`
