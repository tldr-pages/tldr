# transfersh

> A transfer.sh nem hivatalos parancssori kliense. További információ: <https://github.com/AlpixTM/transfersh>.

- Fájl feltöltése a transfer.sh-ba:

`transfersh {{path/to/file}}`

- Fájl feltöltése, amely egy előrehaladási sávot mutat (Python-csomagot igényel: `requests_toolbelt`):

`transfersh --progress {{path/to/file}}`

- Fájl feltöltése más fájlnévvel:

`transfersh --name {{filename}} {{path/to/file}}`

- Fájl feltöltése egy egyéni transfer.sh kiszolgálóra:

`transfersh --servername {{upload.server.name}} {{path/to/file}}`

- Egy könyvtár összes fájljának rekurzív feltöltése:

`transfersh --recursive {{path/to/directory/}}`

- Egy adott könyvtár feltöltése tömörítetlen tar fájlként:

`transfersh -rt {{path/to/directory}}`
