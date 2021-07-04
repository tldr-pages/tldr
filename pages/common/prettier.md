# prettier

> An opinionated code formatter for JavaScript, JSON, CSS, YAML, and more.
> More information: <https://prettier.io/>.

- Format a file and print the result to stdout:

`prettier {{/path/to/file}}`

- Check if a specific file has been formatted:

`prettier --check {{/path/to/file}}`

- Run with a specific configuration file:

`prettier --config {{/path/to/config_file}} {{/path/to/file}}`

- Format a file in place:

`prettier --write {{/path/to/file}}`

- Format all JavaScript files in the current directory recursively:

`prettier --write '*.js'
