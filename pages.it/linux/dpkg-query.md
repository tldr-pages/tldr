# dpkg-query

> Mostra informazioni sui pacchetti installati.
> Maggiori informazioni: <https://manned.org/dpkg-query>.

- Elenca tutti i pacchetti installati:

`dpkg-query {{[-l|--list]}}`

- Elenca i pacchetti installati che corrispondono a un pattern:

`dpkg-query {{[-l|--list]}} '{{libc6*}}'`

- Elenca tutti i file installati da un pacchetto:

`dpkg-query {{[-L|--listfiles]}} {{libc6}}`

- Mostra informazioni su un pacchetto:

`dpkg-query {{[-s|--status]}} {{libc6}}`

- Cerca i pacchetti che possiedono file corrispondenti a un pattern:

`dpkg-query {{[-S|--search]}} {{/etc/ld.so.conf.d}}`
