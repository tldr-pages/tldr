# gifsicle

> GIF manipulátor. További információ: <https://www.lcdf.org/gifsicle>.

- GIF optimalizálása új fájlként:

`gifsicle {{path/to/input.gif}} --optimize=3 -o {{path/to/output.gif}}`

- GIF optimalizálásának feloldása a helyén:

`gifsicle -b {{path/to/input.gif}} --unoptimize`

- Képkocka kivonása egy GIF-ből:

`gifsicle {{path/to/input.gif}} '#{{0}}' > {{path/to/firstframe.gif}}`

- GIF-animáció készítése kiválasztott GIF-ekből:

`gifsicle {{*.gif}} --delay={{10}} --loop > {{path/to/output.gif}}`

- A fájl méretének csökkentése veszteséges tömörítéssel:

`gifsicle -b {{path/to/input.gif}} --optimize=3 --lossy={{100}} --colors={{16}} --dither`

- Az első 10 képkocka és a 20. képkocka utáni összes képkocka törlése egy GIF-ből:

`gifsicle -b {{path/to/input.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- Egy GIF összes képkockájának módosítása meghatározott transzformációs beállításokkal:

`gifsicle -b --crop {{50}},{{50}}+{{-50}}x{{-50}} --scale {{0.25}} --flip-horizontal --rotate-90 {{path/to/input.gif}}`
