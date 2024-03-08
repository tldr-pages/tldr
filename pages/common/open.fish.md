# open

> Opens files, directories, and URIs with default applications.
> This command is available through fish on operating systems without the built-in `open` command (e.g. Haiku and macOS).
> More information: <https://fishshell.com/docs/current/cmds/open.html>.

- Open a file with the associated application:

`open {{path/to/file.ext}}`

- Open all the files of a given extension in the current directory with the associated application:

`open {{*.ext}}`

- Open a directory using the default file manager:

`open {{path/to/directory}}`

- Open a website using the default web browser:

`open {{https://example.com}}`

- Open a specific URI using the default application that can handle it:

`open {{tel:123}}`
