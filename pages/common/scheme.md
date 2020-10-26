# scheme

> MIT Scheme language interperter and REPL (interactive shell).
> More information: <https://www.gnu.org/software/mit-scheme>.

- Open an interactive shell (REPL):

`scheme`

- Run a scheme program (with no REPL output):

`scheme --quiet < {{script.scm}}`

- Load a scheme program into the REPL:

`scheme --load {{script.scm}}`

- Load scheme expressions into the REPL:

`scheme --eval "{{(define foo 'x)}}"`

- Open the REPL in quiet mode:

`scheme --quiet`
