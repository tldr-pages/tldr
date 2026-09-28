# pkgctl diff

> Confronta file di pacchetti usando diverse modalità.
> Vedi anche: `pkgctl`.
> Maggiori informazioni: <https://manned.org/pkgctl-diff>.

- Confronta file di pacchetti in modalità lista contenuti tar (predefinita):

`pkgctl diff {{[-l|--list]}} {{percorso/del/file|nome_pkg}}`

- Confronta file di pacchetti in modalità diffoscope:

`pkgctl diff {{[-d|--diffoscope]}} {{percorso/del/file|nome_pkg}}`

- Confronta file di pacchetti in modalità `.PKGINFO`:

`pkgctl diff {{[-p|--pkginfo]}} {{percorso/del/file|nome_pkg}}`

- Confronta file di pacchetti in modalità `.BUILDINFO`:

`pkgctl diff {{[-b|--buildinfo]}} {{percorso/del/file|nome_pkg}}`
