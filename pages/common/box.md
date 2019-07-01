# box

> A PHP application for building and managing Phars.
> More information: <https://box-project.github.io/box2>.

- Build a new Phar file:

`box build`

- Build a new Phar file using a specific config file:

`box build -c {{path/to/config}}`

- Display information about the PHAR PHP extension:

`box info`

- Display information about a specific Phar file:

`box info {{path/to/phar_file}}`

- Validate the first found config file in the working directory:

`box validate`

- Verify the signature of a specific Phar file:

`box verify {{path/to/phar_file}}`

- Display all available commands and options:

`box help`
