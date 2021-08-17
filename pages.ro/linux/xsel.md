# xsel

> instrument de selectare X11 și manipulare clipboard.

- Utilizați ieșirea unei comenzi ca intrare a clip[b]oard-ului (echivalent cu `Ctrl + C`):

`echo 123 | xsel -ib`

- Utilizați conținutul unui fișier ca intrare a clipboard-ului:

`cat {{file}} | xsel -ib`

- Ieșiți conținutul clipboard-ului în terminal (echivalent cu `Ctrl + V`):

`xsel -ob`

- Ieșiți conținutul clipboard-ului într-un fișier:

`xsel -ob > {{file}}`

- Ștergeți clipboard-ul:

`xsel -cb`

- Ieșiți conținutul selecției primare X11 în terminal (echivalent cu un clic mijlociu al mouse-ului):

`xsel -op`
