# xsel

> Outil de sélection et de manipulation du presse-papiers X11.
> Plus d'informations : <https://manned.org/xsel>.

- Utilise la sortie d'une commande comme entrée du presse-papiers (équivalent de `Ctrl + C`) :

`echo {{123}} | xsel -ib`

- Utilise le contenu d'un fichier comme entrée du presse-papiers :

`cat {{fichier}} | xsel -ib`

- Affiche le contenu du presse-papiers dans le terminal (équivalent à `Ctrl + V`) :

`xsel -ob`

- Sortie du contenu du presse-papiers dans un fichier :

`xsel -ob > {{fichier}}`

- Efface le presse-papiers :

`xsel -cb`

- Affiche le contenu de la sélection primaire X11 dans le terminal (équivalent à un clic du milieu de la souris) :

`xsel -op`
