# xclip

> Outil de manipulation de presse-papiers X11, semblable à `xsel`.
> Gère les sélections primaires et secondaires de X, en plus du presse-papier système (`Ctrl + C`/`Ctrl + V`).
> Plus d'informations : <https://manned.org/xclip>.

- Copie la sortie d'une commande vers la zone de sélection primaire de X11 (presse-papiers) :

`echo 123 | xclip`

- Copie la sortie d'une commande vers une zone de sélection de X11 donnée :

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- Copie le contenu d'un fichier vers le presse-papiers système, avec la notation courte :

`echo 123 | xclip -sel clip`

- Copie le contenu d'un fichier vers le presse-papiers système :

`xclip -sel clip {{fichier_entrée.txt}}`

- Copie le contenu d'une image PNG vers le presse-papiers système (peut être collé dans d'autres programmes correctement) :

`xclip -sel clip -t image/png {{fichier_entrée.png}}`

- Colle le contenu de la zone de sélection de X11 à la console :

`xclip -o`

- Colle le contenu du presse-papier système à la console :

`xclip -o -sel clip`

- Colle le contenu du presse-papier système à un fichier :

`xclip -o -sel clip > {{fichier_sortie.txt}}`
