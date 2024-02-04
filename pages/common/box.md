# box

> A PHP application for building and managing Phars.
> More information: <https://github.com/box-project/box>.

- Compile a new Phar file:

`box compile`

- Compile a new Phar file using a specific configuration file:

`box compile -c {{path/to/config}}`

- Display information about the PHAR PHP extension:

`box info`

- Display information about a specific Phar file:

`box info {{path/to/phar_file}}`

- Validate the first found configuration file in the working directory:

`box validate`

- Verify the signature of a specific Phar file:

`box verify {{path/to/phar_file}}`

- Display help:

`box help`
