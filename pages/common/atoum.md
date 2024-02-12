# atoum

> A simple, modern and intuitive unit testing framework for PHP.
> More information: <http://atoum.org>.

- Initialize a configuration file:

`atoum --init`

- Run all tests:

`atoum`

- Run tests using the specified [c]onfiguration file:

`atoum -c {{path/to/file}}`

- Run a specific test [f]ile:

`atoum -f {{path/to/file}}`

- Run a specific [d]irectory of tests:

`atoum -d {{path/to/directory}}`

- Run all tests under a specific name[s]pace:

`atoum -ns {{namespace}}`

- Run all tests with a specific [t]ag:

`atoum -t {{tag}}`

- Load a custom bootstrap file before running tests:

`atoum --bootstrap-file {{path/to/file}}`
