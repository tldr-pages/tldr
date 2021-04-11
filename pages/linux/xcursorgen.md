# xcursorgen

> Create an X cursor file from a collection of PNG images.
> If `--prefix` is omitted, the image files must be located in the current working directory.
> More information: <https://manned.org/xcursorgen.1>.

- Create an X cursor file using a config file:

`xcursorgen {{path/to/config.cursor}} {{path/to/output_file}}`

- Create an X cursor file using a config file and specify the path to the image files:

`xcursorgen --prefix {{path/to/image_directory/}} {{path/to/config.cursor}} {{path/to/output_file}}`

- Create an X cursor file using a config file and write the output to stdout:

`xcursorgen {{path/to/config.cursor}}`
