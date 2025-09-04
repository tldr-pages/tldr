# rankmirrors

> Classifica una lista di mirror di Pacman in base alla velocità di connessione e apertura.
> Scrive la nuova lista di mirror su `stdout`.
> Maggiori informazioni: <https://manned.org/rankmirrors>.

- Classifica una lista di mirror:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- Mostra solo un certo numero di server con il punteggio più alto:

`rankmirrors -n {{numero}} {{/etc/pacman.d/mirrorlist}}`

- Mostra output dettagliato durante la generazione della lista di mirror:

`rankmirrors {{[-v|--verbose]}} {{/etc/pacman.d/mirrorlist}}`

- Verifica solo un URL specifico:

`rankmirrors {{[-u|--url]}} {{url}}`

- Mostra solo i tempi di risposta invece della lista completa:

`rankmirrors {{[-t|--times]}} {{/etc/pacman.d/mirrorlist}}`
