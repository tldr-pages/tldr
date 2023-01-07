# perl

> The Perl 5 language interpreter.
> More information: <https://www.perl.org>.

- Parse and execute a Perl script:

`perl {{script.pl}}`

- Check syntax errors on a Perl script:

`perl -c {{script.pl}}`

- Parse and execute a Perl statement:

`perl -e {{perl_statement}}`

- Run a Perl script in debug mode, using `perldebug`:

`perl -d {{script.pl}}`

- Edit all file lines [i]n-place with a specific replacement [e]xpression, saving a backup with a new extension:

`perl -p -i'.{{extension}}' -e 's/{{regular_expression}}/{{replacement}}/g' {{path/to/file}}`

- Run a multi-line replacement [e]xpression on a file, and save the result in a specific file:

`perl -p -e 's/{{foo\nbar}}/{{foobar}}/g' {{path/to/input_file}} > {{path/to/output_file}}`

- Run a regular [e]xpression on `stdin`, printing matching [l]ines:

`cat {{path/to/file}} | perl -n -l -e 'print if /{{regular_expression}}/'`

- Run a regular [e]xpression on `stdin`, printing only the first capture group for each matching [l]ine:

`cat {{path/to/file}} | perl -n -l -e 'print $1 if /{{before}}({{regular_expression}}){{after}}/'`
