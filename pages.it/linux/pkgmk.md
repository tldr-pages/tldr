# pkgmk

> Crea un pacchetto binario per l'uso con pkgadd su CRUX.
> Maggiori informazioni: <https://docs.oracle.com/cd/E88353_01/html/E37839/pkgmk-1.html>.

- Crea e scarica un pacchetto:

`pkgmk -d`

- Installa il pacchetto dopo averlo creato:

`pkgmk -d -i`

- Aggiorna il pacchetto dopo averlo creato:

`pkgmk -d -u`

- Ignora l'impronta durante la creazione di un pacchetto:

`pkgmk -d -if`

- Ignora la somma MD5 durante la creazione di un pacchetto:

`pkgmk -d -im`

- Aggiorna l'impronta del pacchetto:

`pkgmk -uf`
