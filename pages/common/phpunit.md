# phpunit

> PHPUnit test runner.
> More information: <https://docs.phpunit.de/en/12.4/textui.html#command-line-options>.

- Run tests in the current directory. Note: Expects you to have a 'phpunit.xml':

`phpunit`

- Run tests in a specific file:

`phpunit {{path/to/TestFile.php}}`

- Run tests annotated with the given group:

`phpunit --group {{name}}`

- Run tests and generate a coverage report in HTML:

`phpunit --coverage-html {{path/to/directory}}`
