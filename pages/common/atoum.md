# atoum

> A simple, modern and intuitive unit testing framework for PHP.
> More information: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- Initialize a configuration file:

`atoum --init`

- Run all tests:

`atoum`

- Run tests using the specified configuration file:

`atoum {{[-c|--configuration]}} {{path/to/file}}`

- Run a specific test file:

`atoum {{[-f|--files]}} {{path/to/file}}`

- Run a specific directory of tests:

`atoum {{[-d|--directories]}} {{path/to/directory}}`

- Run all tests under a specific namespace:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Run all tests with a specific tag:

`atoum {{[-t|--tags]}} {{tag}}`

- Load a custom bootstrap file before running tests:

`atoum {{[-bf|--bootstrap-file]}} {{path/to/file}}`
