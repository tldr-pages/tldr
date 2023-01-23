# xmodmap

> Segédprogram a billentyű- és mutatógombok hozzárendelésének módosítására X-ben. További információ: <https://manned.org/xmodmap>.

- A mutató balra és jobbra kattintásának felcserélése:

`xmodmap -e 'pointer = 3 2 1'`

- A billentyűzet egy billentyűjének átcsoportosítása egy másik billentyűhöz:

`xmodmap -e 'keycode {{keycode}} = {{keyname}}'`

- A billentyűzet egy billentyűjének letiltása:

`xmodmap -e 'keycode {{keycode}} ='`

- A megadott fájlban lévő összes xmodmap-kifejezés végrehajtása:

`xmodmap {{path/to/file}}`
