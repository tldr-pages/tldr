# rich

> A Rich CLI egy eszköztár a terminálban történő fantáziadús kimenethez. További információ: <https://github.com/Textualize/rich-cli>.

- Egy fájl megjelenítése szintaxis-kiemeléssel:

`rich {{path/to/file.py}}`

- Sorszámok és behúzási útmutatók hozzáadása:

`rich {{path/to/file.py}} --line-number --guides`

- Téma alkalmazása:

`rich {{path/to/file.py}} --theme {{monokai}}`

- Egy fájl megjelenítése interaktív lapozóban:

`rich {{path/to/file.py}} --pager`

- Tartalom megjelenítése egy URL-címről:

`rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager`

- Fájl exportálása HTML-ként:

`rich {{path/to/file.md}} --export-html {{path/to/file.html}}`

- Szöveg megjelenítése formázási címkékkel, egyéni igazítással és sorszélességgel:

`rich --print {{"Hello [green on black]Stylized[/green on black] [bold]World[/bold]"}} --{{left|center|right}} --width {{10}}`
