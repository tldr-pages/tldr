# racket

> Racket nyelvi tolmács. További információ: <https://racket-lang.org>.

- REPL (interaktív shell) indítása:

`racket`

- Egy Racket-szkript végrehajtása:

`racket {{path/to/script.rkt}}`

- Racket-kifejezés végrehajtása:

`racket --eval "{{expression}}"`

- Modul futtatása szkriptként (az opciós lista lezárása):

`racket --lib {{module_name}} --main {{arguments}}`

- REPL (interaktív héj) indítása a `typed/racket` hashlanghoz:

`racket -I typed/racket`
