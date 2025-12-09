# aura

> Package manager Aura: gestore pacchetti sicuro e multilingua per Arch Linux e AUR.
> Maggiori informazioni: <https://github.com/fosskers/aura>.

- Cerca pacchetti dall'AUR:

`aura {{[-As|--aursync --search]}} {{keyword|regex}}`

- Installa un pacchetto dall'AUR:

`aura {{[-A|--aursync]}} {{package}}`

- Aggiorna tutti i pacchetti AUR in modalità verbose e rimuove tutte le dipendenze di compilazione:

`aura {{[-Akua|--aursync --diff --sysupgrade --delmakedeps]}}`

- Installa un pacchetto dai repository ufficiali:

`aura {{[-S|--sync]}} {{package}}`

- Sincronizza e aggiorna tutti i pacchetti dai repository ufficiali:

`aura {{[-Syu|--sync --refresh --sysupgrade]}}`

- Rimuove un pacchetto e le sue dipendenze:

`aura {{[-Rsu|--remove --recursive --unneeded]}} {{package}}`

- Rimuove i pacchetti orfani (installati come dipendenze ma non più richiesti):

`aura {{[-Oj|--orphans --abandon]}}`
