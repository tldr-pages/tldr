# du

> Lemezhasználat: a fájl- és könyvtárterület használatának becslése és összegzése. További információ: <https://www.gnu.org/software/coreutils/du>.

- Egy könyvtár és az alkönyvtárak méretének listázása a megadott egységben (B/KiB/MiB):

`du -{{b|k|m}} {{path/to/directory}}`

- Egy könyvtár és az alkönyvtárak méretének listázása, ember által olvasható formában (azaz minden mérethez automatikusan kiválasztja a megfelelő mértékegységet):

`du -h {{path/to/directory}}`

- Egyetlen könyvtár méretének megjelenítése ember által olvasható egységekben:

`du -sh {{path/to/directory}}`

- Egy könyvtár és az abban található összes fájl és könyvtár méretének felsorolása ember által olvasható egységekben:

`du -ah {{path/to/directory}}`

- Egy könyvtár és az alkönyvtárak ember által olvasható méretének listázása, legfeljebb N szint mélységig:

`du -h --max-depth=N {{path/to/directory}}`

- Az aktuális könyvtár alkönyvtáraiban található összes `.jpg` fájl ember által olvasható méretének listázása, és a végén egy összesített összeg megjelenítése:

`du -ch {{*/*.jpg}}`
