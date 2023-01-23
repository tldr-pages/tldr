# dust

> A Dust azonnali áttekintést ad arról, hogy mely könyvtárak használják a lemezterületet. További információ: <https://github.com/bootandy/dust>.

- Az aktuális könyvtár információinak megjelenítése:

`dust`

- A könyvtárak szóközzel elválasztott listájára vonatkozó információk megjelenítése:

`dust {{path/to/directory1}} {{path/to/directory2}}`

- 30 könyvtár megjelenítése (alapértelmezés szerint 21):

`dust --number-of-lines {{30}}`

- Az aktuális könyvtár információinak megjelenítése, legfeljebb 3 szint mélységig:

`dust --depth {{3}}`

- A legnagyobb könyvtárak megjelenítése a tetején, csökkenő sorrendben:

`dust --reverse`

- Az összes adott nevű fájl és könyvtár figyelmen kívül hagyása:

`dust --ignore-directory {{file_or_directory_name}}`

- Ne jelenítsen meg százalékos sávokat és százalékokat:

`dust --no-percent-bars`
