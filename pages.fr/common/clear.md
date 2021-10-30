# clear

> Efface l'écran du terminal.
> Plus d'informations : <https://manned.org/clear>.

- Effacer l'écran (identique à la séquence Contrôle-L sur une interface bash) :

`clear`

- Effacer l'écran mais conserve le tampon de défilement du terminal :

`clear -x`

- Indiquer le type de terminal à effacer (utilise par défaut la variable d'environnement `TERM`) :

`clear -T {{type_de_terminal}}`

- Afficher la version de `ncurses` utilisée par `clear` :

`clear -V`
