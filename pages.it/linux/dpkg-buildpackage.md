# dpkg-buildpackage

> Compila pacchetti Debian binari e/o sorgenti dal codice sorgente.
> Normalmente eseguito all'interno di un albero sorgente che contiene una directory `debian/`.
> Gestisce anche le dipendenze di compilazione, crea file come `.buildinfo` e `.changes` e firma il risultato se applicabile.
> Maggiori informazioni: <https://manned.org/dpkg-buildpackage>.

- Genera pacchetti sorgente e binari:

`dpkg-buildpackage`

- Genera solo pacchetti binari (nessun pacchetto sorgente):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- Genera solo il pacchetto sorgente (senza compilare binari):

`dpkg-buildpackage {{[-S|--build=source]}}`

- Non firmare i file `.dsc` e `.changes`:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- Non eseguire `clean` prima della compilazione:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- Usa `fakeroot` come comando per ottenere privilegi di root durante la compilazione:

`dpkg-buildpackage {{[-r|--root-command=]}}fakeroot`

- Esegue un target specifico di `debian/rules`:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
