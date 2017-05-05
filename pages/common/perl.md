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

- Loo[p] over all lines of a file, editing them [i]n-place using a find/replace [e]xpression:

`perl -p -i -e 's/{{find}}/{{replace}}/g' {{filename}}`

- Run a find/replace expression on a file, saving the original file with a given extension:

`perl -p -i'.old' -e 's/{{find}}/{{replace}}/g' {{filename}}`
