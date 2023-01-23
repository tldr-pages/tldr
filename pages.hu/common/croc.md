# croc

> Küldjön és fogadjon fájlokat egyszerűen és biztonságosan bármilyen hálózaton keresztül. További információ: <https://github.com/schollz/croc>.

- Fájl vagy könyvtár küldése:

`croc send {{path/to/file_or_directory}}`

- Fájl vagy könyvtár küldése egy adott jelszóval:

`croc send --code {{passphrase}} {{path/to/file_or_directory}}`

- Fájl vagy könyvtár fogadása a fogadó gépen:

`croc {{passphrase}}`

- Küldés és kapcsolódás egyéni relén keresztül:

`croc --relay {{ip_to_relay}} send {{path/to/file_or_directory}}`

- Fogadás és csatlakozás egy egyéni relén keresztül:

`croc --relay {{ip_to_relay}} {{passphrase}}`

- Croc relé fogadása az alapértelmezett portokon:

`croc relay`

- A croc parancs paramétereinek és opcióinak megjelenítése:

`croc {{send|relay}} --help`
