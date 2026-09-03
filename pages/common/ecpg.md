# ecpg

> Embedded SQL preprocessor for C programs.
> More information: <https://www.postgresql.org/docs/current/app-ecpg.html>.

- Preprocess a specific file:

`ecpg {{path/to/input.pgc}}`

- Preprocess from `stdin` and output to `stdout`:

`ecpg -o - -`

- Preprocess from `stdin` and write to a file:

`cat {{path/to/input.pgc}} | ecpg -o {{path/to/output.c}} -`

- Preprocess and specify an output file:

`ecpg {{path/to/input.pgc}} -o {{path/to/output.c}}`

- Preprocess a header file (`.pgh` extension):

`ecpg {{path/to/input.pgh}}`

- Preprocess in a specific compatibility mode:

`ecpg {{path/to/input.pgc}} -C {{INFORMIX|INFORMIX_SE|ORACLE}}`

- Preprocess with autocommit enabled:

`ecpg {{path/to/input.pgc}} -t`
