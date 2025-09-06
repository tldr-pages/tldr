# getopt

> Parse command-line arguments.
> More information: <https://manned.org/getopt>.

- Parse optional `verbose`/`version` flags with shorthands:

`getopt {{[-o|--options]}} vV {{[-l|--longoptions]}} verbose,version -- --version --verbose`

- Add a `--file` option with a required argument with shorthand `-f`:

`getopt {{[-o|--options]}} f: {{[-l|--longoptions]}} file: -- --file=somefile`

- Add a `--verbose` option with an optional argument with shorthand `-v`, and pass a non-option parameter `arg`:

`getopt {{[-o|--options]}} v:: {{[-l|--longoptions]}} verbose:: -- --verbose arg`

- Accept a `-r` and `--verbose` flag, a `--accept` option with an optional argument and add a `--target` with a required argument option with shorthands:

`getopt {{[-o|--options]}} rv::s::t: {{[-l|--longoptions]}} verbose,source::,target: -- -v --target target`
