# clear

> Leert den Bildschirm eines Terminals.
> Weitere Informationen: <https://manned.org/clear>.

- Leere den Bildschirm (äquivalent zu `<Ctrl l>` in einer Bash Shell):

`clear`

- Leere den Bildschirm, aber erhalte den Rückscroll-Puffer des Terminals:

`clear -x`

- Lege den Typ des zu leerenden Terminals fest (Standardwert ist die Umgebungsvariable $TERM):

`clear -T {{typ_des_terminals}}`

- Zeige die Version von `ncurses` an, die von `clear` benutzt wird:

`clear -V`
