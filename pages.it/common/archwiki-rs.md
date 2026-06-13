# archwiki-rs

> Leggi, cerca e scarica pagine dall'ArchWiki.
> Maggiori informazioni: <https://gitlab.com/lucifayr/archwiki-rs>.

- Leggi una pagina dall'ArchWiki:

`archwiki-rs read-page {{titolo_pagina}}`

- Leggi una pagina dall'ArchWiki nel formato specificato:

`archwiki-rs read-page {{titolo_pagina}} --format {{plain-text|markdown|html}}`

- Cerca nell'ArchWiki pagine contenenti il testo fornito:

`archwiki-rs search "{{testo_di_ricerca}}" --text-search`

- Scarica una copia locale di tutte le pagine ArchWiki in una directory specifica:

`archwiki-rs local-wiki /{{percorso/wiki_locale}} --format {{plain-text|markdown|html}}`
