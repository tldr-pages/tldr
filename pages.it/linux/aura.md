# aura

> Package manager Aura: gestore pacchetti sicuro e multilingua per Arch Linux e AUR.
> Maggiori informazioni: <https://github.com/fosskers/aura>.

- Cerca pacchetti dall'AUR:

`aura -As {{keyword|regex}}`

- Installa un pacchetto dall'AUR:

`aura -A {{package}}`

- Aggiorna tutti i pacchetti AUR in modalità verbose e rimuove tutte le dipendenze di compilazione:

`aura -Akua`

- Installa un pacchetto dai repository ufficiali:

`aura -S {{package}}`

- Sincronizza e aggiorna tutti i pacchetti dai repository ufficiali:

`aura -Syu`

- Rimuove un pacchetto e le sue dipendenze:

`aura -Rsu {{package}}`

- Rimuove i pacchetti orfani (installati come dipendenze ma non più richiesti):

`aura -Oj`
