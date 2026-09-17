# agy

> An agentic development platform by Google.
> More information: <https://antigravity.google/docs>.

- Open a specific file or directory:

`agy {{path/to/file_or_directory}}`

- Compare two files with each other:

`agy {{[-d|--diff]}} {{path/to/file1}} {{path/to/file2}}`

- Pass in a prompt to run in a chat session in the current working directory:

`agy chat "{{prompt}}"`

- Install or uninstall a specific extension:

`agy --{{install|uninstall}}-extension {{publisher.extension|path/to/extension.vsix}}`

- Add an MCP (Model Context Protocol) server definition to the user profile:

`agy --add-mcp "{{json_string}}"`

- Display help:

`agy {{[-h|--help]}}`
