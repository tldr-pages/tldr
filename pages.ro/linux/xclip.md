# xclip

> instrument de manipulare clipboard X11, similar cu `xsel`.
> Gestionează selecțiile X primare și secundare, plus clipboard-ul de sistem (`Ctrl + C`/`Ctrl + V`).

- Copiați ieșirea dintr-o comandă în zona de selecție primară X11 (clipboard):

`echo 123 | xclip`

- Copiați ieșirea dintr-o comandă într-o anumită zonă de selecție X11:

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- Copiați ieșirea dintr-o comandă în clipboard-ul sistemului, folosind notație scurtă:

`echo 123 | xclip -sel clip`

- Copiați conținutul unui fișier în clipboard-ul sistemului:

`xclip -sel clip {{input_file.txt}}`

- Copiați conținutul unei imagini PNG în clipboard-ul sistemului (poate fi lipit corect în alte programe):

`xclip -sel clip -t image/png {{input_file.png}}`

- Copiați intrarea utilizatorului în consola în clipboard-ul sistemului:

`xclip -i`

- Lipiţi conţinutul zonei principale de selecţie X11 pe consola:

`xclip -o`

- Lipiți conținutul clipboard-ului de sistem în consola:

`xclip -o -sel clip`
