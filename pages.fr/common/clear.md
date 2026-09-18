# clear

> Efface l'écran du terminal.
> Plus d'informations : <https://manned.org/clear>.

- Efface l'écran (identique à la séquence `<Ctrl l>` sur une interface Bash) :

`clear`

- Efface l'écran mais conserve le tampon de défilement du terminal :

`clear -x`

- Indique le type de terminal à effacer (utilise par défaut la variable d'environnement `$TERM`) :

`clear -T {{type_de_terminal}}`

- Affiche la version de `ncurses` utilisée par `clear` :

`clear -V`
