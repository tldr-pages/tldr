# atoum

> A simple, modern and intuitive unit testing framework for PHP.
> More information: <http://atoum.org>.

- Initialise a configuration file:

`atoum --init`

- Run all tests:

`atoum`

- Run tests using the specified configuration file:

`atoum -c {{path/to/file}}`

- Run a specific test file:

`atoum -f {{path/to/file}}`

- Run a specific directory of tests:

`atoum -d {{path/to/directory}}`

- Run all tests under a specific namespace:

`atoum -ns {{namespace}}`

- Run all tests with a specific tag:

`atoum -t {{tag}}`

- Load a custom bootstrap file before running tests:

`atoum --bootstrap-file {{path/to/file}}`
