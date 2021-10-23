# getopt

> Parse command line arguments.
> More information: <https://www.gnu.org/software/libc/manual/html_node/Getopt.html>.

- Parse optional `verbose`/`version` flags with shorthands:

`getopt -o vV --longoptions verbose,version -- --version --verbose`

- Add a `--file` option with a required argument with shorthand `-f`:

`getopt -o f: --longoptions file: -- --file=somefile`

- Add a `--verbose` option with an optional argument with shorthand `-v`, and pass a non-option parameter `arg`:

`getopt -o v:: --longoptions verbose:: -- --verbose arg`

- Accept a `-r` and `--verbose` flag, a `--accept` option with an optional argument and add a `--target` with a required argument option with shorthands:

`getopt -o rv::s::t: --longoptions verbose,source::,target: -- -v --target target`
