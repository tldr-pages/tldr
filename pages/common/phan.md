# phan

> A static analysis tool for PHP.
> More information: <https://github.com/phan/phan>.

- Generate a `.phan/config.php` in the current directory:

`phan --init`

- Generate a Phan configuration file using a specific level (1 being strictest to 5 being the least strict):

`phan --init --init-level {{level}}`

- Analyse the current directory:

`phan`

- Analyse one or more directories:

`phan --directory {{path/to/directory}} --directory {{path/to/another_directory}}`

- Specify a config file (defaults to `.phan/config.php`):

`phan --config-file {{path/to/config.php}}`

- Specify the output mode:

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- Specify the number of parallel processes:

`phan --processes {{number_of_processes}}`
