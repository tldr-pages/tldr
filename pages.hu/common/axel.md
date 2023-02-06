# axel

> Letöltésgyorsító. Támogatja a HTTP, HTTPS és FTP protokollokat. További információ: <https://github.com/axel-download-accelerator/axel>.

- URL letöltése egy fájlba:

`axel {{url}}`

- Letöltés és fájlnév megadása:

`axel {{url}} -o {{path/to/file}}`

- Letöltés több kapcsolattal:

`axel -n {{connections_num}} {{url}}`

- Tükörképek keresése:

`axel -S {{mirrors_num}} {{url}}`

- Letöltési sebesség korlátozása (bájt/másodperc):

`axel -s {{speed}} {{url}}`
