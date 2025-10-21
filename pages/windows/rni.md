# rni

> Powershell command to rename an item.
> This command is an alias of `Rename-Item`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-item>.

- Rename a file:

`rni -Path "{{path/to/file}}" -NewName "{{new_file_name}}"`

- Rename a directory:

`rni -Path "{{path/to/directory}}" -NewName "{{new_directory_name}}"`

- Rename and move a file:

`rni -Path "{{path/to/file}}" -NewName "{{path/to/new_file_name}}"`

- Rename a file by force:

`rni -Path "{{path/to/file}}" -NewName "{{new_file_name}}" -Force`

- Prompt comfirmation before renaming a file:

`rni -Path "{{path/to/file}}" -NewName "{{new_file_name}}" {{[-Confirm|-cf]}}`
