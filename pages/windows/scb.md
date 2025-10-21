# scb

> Powershell command to set content to clipboard.
> This command is an alias of `Set-Clipboard`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-clipboard>.

- Copy text to the clipboard:

`scb -Value "{{text}}"`

- Copy multiple texts to clipboard separated by new line:

`scb -Value @("{{text 1}}", "{{text 2}}", "{{text 3}}")`

- Copy files or directories to clipboard:

`scb -Path "{{path/to/files_or_directories}}"`

- Copy multiple files:

`scb -Path "{{path/to/file1}}","{{path/to/file2}}","{{path/to/file3}}"`

- To clear the clipboard:

`scb ""`
