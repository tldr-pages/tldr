# raku

> Rakudo Raku (formerly Perl 6) programming language interpreter.
> See also: `perl`.
> More information: <https://manned.org/raku>.

- Execute a Raku script:

`raku {{path/to/script.raku}}`

- Execute a single Raku command:

`raku -e "{{command}}"`

- Check syntax only (runs BEGIN and CHECK blocks):

`raku -c {{path/to/script.raku}}`

- Start a REPL (interactive shell):

`raku`

- Load a module before running the program:

`raku -M {{module_name}} {{path/to/script.raku}}`

- Add a path to the module search path:

`raku -I {{path/to/module_directory}} {{path/to/script.raku}}`

- Extract and display documentation from a script:

`raku --doc {{path/to/script.raku}}`
