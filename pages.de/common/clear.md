# clear

> Leert den Bildschirm eines Terminals.

- Leert den Bildschirm (äquivalent zu Strg+L in einer Bash Shell):

`clear`

- Leert den Bildschirm, aber erhält den Rückscroll-Puffer des Terminals:

`clear -x`

- Legt den Typ des zu leerendes Terminals fest (Standardwert ist die Umgebungsvariable $TERM):

`clear -T {{typ_des_terminals}}`

- Zeigt die Version von `ncurses` an, die von `clear` benutzt wird:

`clear -V`
