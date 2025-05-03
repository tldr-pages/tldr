# racket

> Racket language interpreter.
> More information: <https://docs.racket-lang.org/reference/running-sa.html#%28part._mz-cmdline%29>.

- Start a REPL (interactive shell):

`racket`

- Execute a Racket script:

`racket {{path/to/script.rkt}}`

- Execute a Racket expression:

`racket {{[-e|--eval]}} "{{expression}}"`

- Run module as a script (terminates option list):

`racket {{[-l|--lib]}} {{module_name}} {{[-m|--main]}} {{arguments}}`

- Start a REPL (interactive shell) for the `typed/racket` hashlang:

`racket -I typed/racket`
