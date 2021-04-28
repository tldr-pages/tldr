# mocha

> Execute Mocha JavaScript test runner.
> More information: <https://mochajs.org>.

- Run tests with default configuration or as configured in `mocha.opts`:

`mocha`

- Run tests contained at a specific location:

`mocha {{directory/with/tests}}`

- Run tests that match a specific grep pattern:

`mocha --grep {{regular_expression}}`

- Run tests on changes to JavaScript files in the current directory and once initially:

`mocha --watch`

- Run tests with a specific reporter:

`mocha --reporter {{reporter}}`
