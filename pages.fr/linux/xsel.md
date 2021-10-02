# xsel

> Outil de sélection et de manipulation du presse-papiers X11.

- Utiliser la sortie d'une commande comme entrée du presse-papiers (équivalent de `Ctrl + C`) :

`echo 123 | xsel -ib`

- Utiliser le contenu d'un fichier comme entrée du presse-papiers :

`cat {{fichier}} | xsel -ib`

- Affiche le contenu du presse-papiers dans le terminal (équivalent à `Ctrl + V`) :

`xsel -ob`

- Sortie du contenu du presse-papiers dans un fichier :

`xsel -ob > {{fichier}}`

- Effacer le presse-papiers :

`xsel -cb`

- Affiche le contenu de la sélection primaire X11 dans le terminal (équivalent à un clic du milieu de la souris) :

`xsel -op`
