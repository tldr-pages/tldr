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

- Edit all file lines [i]n-place with a specific replacement [e]xpression and save a file with a new extension:

`perl -p -i'.{{extension}}' -e 's/{{regular_expression}}/{{replacement}}/g' {{path/to/file}}`

- Run a multi-line replacement expression on a file, and save the result in a specific file:

`perl -p -e 's/{{foo\nbar}}/{{foobar}}/g' {{input_file}} > {{output_file}}`

- Run a regular expression on stdin, printing out matching [l]ines:

`cat {{filename}} | perl -n -l -e 'print if /{{pattern}}/'`

- Run a regular expression on stdin, printing out only the first capture group for each matching [l]ine:

`cat {{filename}} | perl -n -l -e 'print $1 if /{{before}}({{pattern}}){{after}}/'`
