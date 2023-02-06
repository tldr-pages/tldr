# scheme

> MIT Scheme nyelvi értelmező és REPL (interaktív shell). További információ: <https://www.gnu.org/software/mit-scheme>.

- REPL (interaktív shell) indítása:

`scheme`

- Scheme program futtatása (REPL kimenet nélkül):

`scheme --quiet < {{script.scm}}`

- Scheme program betöltése a REPL-be:

`scheme --load {{script.scm}}`

- Scheme-kifejezések betöltése a REPL-be:

`scheme --eval "{{(define foo 'x)}}"`

- A REPL megnyitása csendes üzemmódban:

`scheme --quiet`
