# ecpg

> Embedded SQL preprocessor for C programs.
> More information: <https://www.postgresql.org/docs/current/app-ecpg.html>.

- Preprocess a specific file:

`ecpg {{input.pgc}}`

- Preprocess from `stdin` and output to `stdout`:

`ecpg -o - -`

- Preprocess from `stdin` and write to a file:

`cat input.pgc | ecpg -o output.c -`

- Preprocess and specify an output file:

`ecpg -o {{output.c}} {{input.pgc}}`

- Preprocess a header file (`.pgh` extension):

`ecpg {{input.pgh}}`

- Preprocess in a specific compatibility mode:

`ecpg -C {{INFORMIX|INFORMIX_SE|ORACLE}} {{input.pgc}}`

- Preprocess with autocommit enabled:

`ecpg -t {{input.pgc}}`
