# mocha

> A feature-rich JavaScript test framework.
> More information: <https://mochajs.org/#command-line-usage>.

- Run tests with default configuration or as configured in `mocha.opts`:

`mocha`

- Run tests contained at a specific location:

`mocha {{path/to/test_directory}}`

- Run tests that match a specific `grep` pattern:

`mocha {{[-g|--grep]}} {{regex}}`

- Run tests on changes to JavaScript files in the current directory and once initially:

`mocha {{[-w|--watch]}}`

- Run tests with a specific reporter:

`mocha {{[-R|--reporter]}} {{reporter}}`
