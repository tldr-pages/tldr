# gyb

> Parancssori eszköz a Gmail üzenetek helyi mentéséhez a Gmail API segítségével HTTPS-en keresztül. További információ: <https://github.com/GAM-team/got-your-back>.

- A Gmail-fiókjában lévő összes e-mail számának és méretének megbecslése:

`gyb --email {{email@gmail.com}} --action estimate`

- Gmail-fiók biztonsági mentése egy adott könyvtárba:

`gyb --email {{email@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- Csak a fontos vagy csillagos e-mailek biztonsági mentése egy Gmail-fiókból az alapértelmezett helyi mappába:

`gyb --email {{email@gmail.com}} --search "{{is:important OR is:starred}}"`

- Helyi mappából történő visszaállítás egy Gmail-fiókba:

`gyb --email {{email@gmail.com}} --action restore --local-folder {{path/to/directory}}`
