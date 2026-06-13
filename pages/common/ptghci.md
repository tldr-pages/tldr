# ptghci

> Interactive Haskell REPL with syntax highlighting, multiline editing, and real-time type display.
> See also: `ghci`.
> More information: <https://github.com/litxio/ptghci>.

- Start an interactive session:

`ptghci`

- Start an interactive session and load a Haskell file:

`ptghci {{path/to/file.hs}}`

- [Interactive] List past commands from the current session:

`%past`

- [Interactive] List past commands including previous sessions:

`%past -n {{number}}`

- [Interactive] Re-run specific commands from history:

`%rerun {{3,4-5,p8}}`

- [Interactive] Search Hoogle for an identifier:

`%hoogle {{identifier}}`

- [Interactive] Change the syntax highlighting style:

`%style {{style_name}}`
