# eselect news

> Un modulo `eselect` per la lettura degli articoli di notizie di Gentoo.
> Nota: Portage stamperà un avviso quando un repository viene sincronizzato e ci sono articoli di notizie non letti.
> Maggiori informazioni: <https://wiki.gentoo.org/wiki/Eselect#News>.

- Elenca gli articoli di notizie disponibili con i loro numeri (tutti di default):

`eselect news list {{all|new}}`

- Stampa gli articoli di notizie specificati:

`eselect news read {{numero1 numero2 ...}}`

- Stampa tutti gli articoli di notizie non letti:

`eselect news read`

- Segna gli articoli di notizie specificati come non letti:

`eselect news unread {{numero1 numero2 ...}}`

- Elimina tutti gli articoli di notizie letti:

`eselect news purge`

- Stampa il numero di articoli di notizie disponibili (nuovi di default):

`eselect news count {{all|new}}`
