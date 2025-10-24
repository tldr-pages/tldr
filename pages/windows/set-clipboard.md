# Set-Clipboard

> Powershell command to set content to clipboard.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-clipboard>.

- Copy text to the clipboard:

`{{[scb|Set-Clipboard]}} -Value "{{text}}"`

- Copy multiple texts to clipboard separated by new line:

`Set-Clipboard -Value @("{{text 1}}", "{{text 2}}", "{{text 3}}")`

- Copy files or directories to clipboard:

`Set-Clipboard -Path "{{path/to/files_or_directories}}"`

- Copy multiple files:

`Set-Clipboard -Path "{{path/to/file1}}","{{path/to/file2}}","{{path/to/file3}}"`

- To clear the clipboard:

`Set-Clipboard ""`
