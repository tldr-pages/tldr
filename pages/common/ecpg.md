# ecpg

> Embedded SQL preprocessor for C programs.
> More information: <https://www.postgresql.org/docs/current/app-ecpg.html>.

- Preprocess a specific file:

`ecpg {{prog1.pgc}}`

- Preprocess from `stdin` and output to `stdout`:

`ecpg -`

- Preprocess and specify an output file:

`ecpg -o {{output.c}} {{input.pgc}}`

- Preprocess a header file (`.pgh` extension):

`ecpg {{input.pgh}}`

- Preprocess in a specific compatibility mode (e.g., INFORMIX):

`ecpg -C {{INFORMIX}} {{input.pgc}}`

- Preprocess with autocommit enabled:

`ecpg -t {{input.pgc}}`