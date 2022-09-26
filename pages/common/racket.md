# racket

> Racket language interpreter.
> More information: <https://racket-lang.org>.

- Start a REPL (interactive shell):

`racket`

- Execute a Racket script:

`racket {{path/to/script.rkt}}`

- Execute a Racket expression:

`racket --eval "{{expression}}"`

- Run module as a script (terminates option list):

`racket --lib {{module_name}} --main {{arguments}}`

- Start a REPL (interactive shell) for the `typed/racket` hashlang:

`racket -I typed/racket`
