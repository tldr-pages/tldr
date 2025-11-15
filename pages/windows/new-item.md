# New-Item

> Create a new file, directory, symbolic link, or a registry entry.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- Create a new blank file (equivalent to `touch`):

`New-Item {{path\to\file}}`

- Create a new directory:

`New-Item -ItemType Directory {{path\to\directory}}`

- Write a new text file with specified content:

`New-Item {{path\to\file}} -Value {{content}}`

- Write the same text file in multiple locations:

`New-Item {{path\to\file1 , path\to\file2 , ...}} -Value {{content}}`

- Create a symbolic link\hard link\junction to a file or directory:

`New-Item -ItemType {{SymbolicLink|HardLink|Junction}} -Path {{path\to\link_file}} -Target {{path\to\source_file_or_directory}}`

- Create a new blank registry entry (in REG_SZ, use `New-ItemProperty` or `Set-ItemProperty` to fine-tune the value type):

`New-Item {{path\to\registry_key}}`

- Create a new blank registry entry with specified value:

`New-Item {{path\to\registry_key}} -Value {{value}}`
