# du

> Lemezhasználat: a fájl- és könyvtárterület használatának becslése és összegzése. További információ: <https://ss64.com/osx/du.html>.

- Egy könyvtár és az alkönyvtárak méretének listázása a megadott egységben (KiB/MiB/GiB):

`du -{{k|m|g}} {{path/to/directory}}`

- Egy könyvtár és az alkönyvtárak méretének listázása ember által olvasható formában (azaz minden mérethez automatikusan kiválasztja a megfelelő mértékegységet):

`du -h {{path/to/directory}}`

- Egyetlen könyvtár méretének megjelenítése ember által olvasható egységekben:

`du -sh {{path/to/directory}}`

- Egy könyvtár és az abban található összes fájl és könyvtár méretének felsorolása ember által olvasható egységekben:

`du -ah {{path/to/directory}}`

- Egy könyvtár és az alkönyvtárak ember által olvasható méretének listázása, legfeljebb N szint mélységig:

`du -h -d {{N}} {{path/to/directory}}`

- Az aktuális könyvtár alkönyvtáraiban található összes `.jpg` fájl ember által olvasható méretének listázása, és a végén egy összesített összeg megjelenítése:

`du -ch {{*/*.jpg}}`
