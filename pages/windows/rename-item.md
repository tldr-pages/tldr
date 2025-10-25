# Rename-Item

> Powershell command to rename an item.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-item>.

- Rename a file:

`Rename-Item -Path "{{path/to/file}}" -NewName "{{new_file_name}}"`

- Rename a directory:

`Rename-Item -Path "{{path/to/directory}}" -NewName "{{new_directory_name}}"`

- Rename and move a file:

`Rename-Item -Path "{{path/to/file}}" -NewName "{{path/to/new_file_name}}"`

- Rename a file by force:

`Rename-Item -Path "{{path/to/file}}" -NewName "{{new_file_name}}" -Force`

- Prompt confirmation before renaming a file:

`Rename-Item -Path "{{path/to/file}}" -NewName "{{new_file_name}}" {{[-Confirm|-cf]}}`
