# pastel

> Színek generálása, elemzése, konvertálása és manipulálása. További információ: <https://github.com/sharkdp/pastel>.

- Színek konvertálása egyik formátumból a másikba. Itt RGB-ből HSL-be:

`pastel format {{hsl}} {{ff8000}}`

- Színek megjelenítése és elemzése a terminálon:

`pastel color "{{rgb(255,50,127)}}"`

- Válasszon ki egy színt valahonnan a képernyőn:

`pastel pick`

- N vizuálisan különböző színből álló készlet generálása:

`pastel distinct {{8}}`

- Az összes X11 / CSS színnév listájának lekérdezése:

`pastel list`
