# scd

> A shell integrációra összpontosító fájlkezelő. További információ: <https://github.com/cshuaimin/scd>.

- Index útvonalak rekurzívan a legelső futtatásnál:

`scd -ar {{path/to/directory}}`

- Váltás egy adott könyvtárba:

`scd {{path/to/directory}}`

- Váltás egy adott mintának megfelelő elérési útvonalra:

`scd "{{pattern1 pattern2 ...}}"`

- Kiválasztási menü megjelenítése és a 20 legvalószínűbb könyvtár rangsorolása:

`scd -v`

- Speciális alias hozzáadása az aktuális könyvtárhoz:

`scd --alias={{word}}`

- Váltás egy könyvtárba egy adott alias használatával:

`scd {{word}}`
