# lpr

> CUPS eszköz fájlok nyomtatására. Lásd még: `lpstat` és `lpadmin`. További információ: <https://www.cups.org/doc/man-lpr.html>.

- Fájl nyomtatása az alapértelmezett nyomtatóra:

`lpr {{path/to/file}}`

- 2 példány nyomtatása:

`lpr -# {{2}} {{path/to/file}}`

- Nyomtatás egy megnevezett nyomtatóra:

`lpr -P {{printer}} {{path/to/file}}`

- Egyetlen oldal (pl. 2) vagy egy oldaltartomány (pl. 2-16) nyomtatása:

`lpr -o page-ranges={{2|2-16}} {{path/to/file}}`

- Kétoldalas nyomtatás vagy függőleges (hosszú), vagy álló (rövid) nyomtatás:

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{path/to/file}}`

- Oldalméret beállítása (a beállításoktól függően több lehetőség is rendelkezésre állhat):

`lpr -o media={{a4|letter|legal}} {{path/to/file}}`

- Több oldal nyomtatása laponként:

`lpr -o number-up={{2|4|6|9|16}} {{path/to/file}}`
