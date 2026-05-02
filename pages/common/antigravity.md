# antigravity

> An agentic development platform by Google.
> More information: <https://antigravity.google/docs>.

- Open specific file or directory:

`antigravity "{{path/to/file_or_directory}}"`

- Compare two files with each other:

`antigravity {{[-d|--diff]}} "{{path/to/file1}}" "{{path/to/file2}}"`

- Pass in a prompt to run in a chat session in the current working directory:

`antigravity chat "{{prompt}}"`

- Install or uninstall a specific extension:

`antigravity --{{install|uninstall}}-extension "{{publisher.extension|path/to/extension.vsix}}"`

- Add a MCP (Model Context Protocol) server definition to the user profile:

`antigravity --add-mcp "{{json_string}}"`

- Display help:

`antigravity {{[-h|--help]}}`
