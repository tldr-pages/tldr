# qcp

> Fájlok másolása az alapértelmezett szövegszerkesztővel a fájlnevek meghatározásához. További információ: <https://www.nongnu.org/renameutils/>.

- Egyetlen fájl másolása (nyisson meg egy szerkesztőt, amelynek bal oldalán a forrásfájl neve, jobb oldalán pedig a célfájl neve található):

`qcp {{source_file}}`

- Több JPG fájl másolása:

`qcp {{*.jpg}}`

- Fájlok másolása, de a forrás- és a célfájlnév pozíciójának felcserélése a szerkesztőben:

`qcp --option swap {{*.jpg}}`
