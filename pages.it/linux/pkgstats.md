# pkgstats

> Invia e visualizza le statistiche di popolarità dei pacchetti di Arch Linux.
> Maggiori informazioni: <https://github.com/archlinux-de/pkgstats-cli#usage>.

- Invia i dati dei pacchetti installati:

`pkgstats submit`

- Visualizza i dati inviati:

`pkgstats submit {{[-d|--dump-json]}}`

- Cerca pacchetti:

`pkgstats search {{termine_ricerca}}`

- Limita il numero di risultati di ricerca (10 per impostazione predefinita):

`pkgstats search {{termine_ricerca}} {{[-l|--limit]}} {{conteggio}}`

- Seleziona pacchetti per il confronto:

`pkgstats show {{pacchetto1 pacchetto2 ...}}`

- Mostra aiuto:

`pkgstats {{[-h|--help]}}`
