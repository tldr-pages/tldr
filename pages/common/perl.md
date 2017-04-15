# perl

> The Perl 5 language interpreter.

- Parse and execute a Perl script:

`perl {{script.pl}}`

- Check syntax errors on a Perl script:

`perl -c {{script.pl}}`

- Parse and execute a perl statement:

`perl -e {{perl_statement}}`

- Import module before execution of a perl statement:

`perl -M{{module}} -e {{perl_statement}}`

- Run a Perl script in debug mode, using `perldebug`:

`perl -d {{script.pl}}`

- Replace all occurrences of a string in a file with another string, overwriting the file in-place:

`perl -p -i -e 's/{{find}}/{{replace}}/g' {{filename}}`

- Same, saving an unmodified copy of the original file with a different extension:

`perl -p -i'.old' -e 's/{{find}}/{{replace}}/g' {{filename}}`
