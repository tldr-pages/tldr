# php-coveralls

> A PHP client for Coveralls.
> More information: <https://php-coveralls.github.io/php-coveralls/#cli-options>.

- Send coverage information to Coveralls:

`php-coveralls`

- Send coverage information to Coveralls for a specific directory:

`php-coveralls {{[-r|--root_dir]}} {{path/to/directory}}`

- Send coverage information to Coveralls with a specific config:

`php-coveralls {{[-c|--config]}} {{path/to/.coveralls.yml}}`

- Send coverage information to Coveralls with verbose output:

`php-coveralls {{[-v|--verbose]}}`

- Send coverage information to Coveralls excluding source files with no executable statements:

`php-coveralls --exclude-no-stmt`

- Send coverage information to Coveralls with a specific environment name:

`php-coveralls {{[-e|--env]}} {{test|dev|prod}}`

- Specify multiple Coverage Clover XML files to upload:

`php-coveralls {{[-x|--coverage_clover]}} {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- Output the JSON that will be sent to Coveralls to a specific file:

`php-coveralls {{[-o|--json_path]}} {{path/to/coveralls-upload.json}}`
