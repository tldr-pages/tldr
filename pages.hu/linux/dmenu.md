# dmenu

> Dinamikus menü. Szövegbevitelből létrehoz egy menüt, amelynek minden egyes eleme egy új sorban található. További információ: <https://manned.org/dmenu>.

- A `ls` parancs kimenetének menüjének megjelenítése:

`{{ls}} | dmenu`

- Egy menü megjelenítése új sorral elválasztott egyéni elemekkel (`\n`):

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu`

- Hagyja, hogy a felhasználó több elem közül válasszon, és a kiválasztottat mentse egy fájlba:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu > {{color.txt}}`

- A dmenu elindítása egy adott monitoron:

`ls | dmenu -m {{1}}`

- A dmenu megjelenítése a képernyő alján:

`ls | dmenu -b`
