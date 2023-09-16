# stylua

> An opinionated Lua code formatter.
> More information: <https://github.com/JohnnyMorganz/StyLua>.

- Auto-format a file or an entire directory:

`stylua {{path/to/file_or_directory}}`

- Check if a specific file has been formatted:

`stylua --check {{path/to/file}}`

- Run with a specific configuration file:

`stylua --config-path {{path/to/config_file}} {{path/to/file}}`

- Format code from `stdin` and output to `stdout`:

`stylua - < {{path/to/file.lua}}`

- Format a file or directory using spaces and preferring single quotes:

`stylua --indent-type {{Spaces}} --quote-style {{AutoPreferSingle}} {{path/to/file_or_directory}}`
