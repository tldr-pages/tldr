# Move-Item

> Move or rename files, directories, registry keys, and other PowerShell data items.
> This command can only be run through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- Rename a file or directory when the target is not an existing directory:

`Move-Item {{path\to\source}} {{path\to\target}}`

- Move a file or directory into an existing directory:

`Move-Item {{path\to\source}} {{path\to\existing_directory}}`

- Rename or move file(s) with specific name (do not treat special characters inside strings):

`Move-Item -LiteralPath "{{path\to\source}}" {{path\to\file_or_directory}}`

- Move multiple files into an existing directory, keeping the filenames unchanged:

`Move-Item {{path\to\source1 , path\to\source2 ...}} {{path\to\existing_directory}}`

- Move or rename registry key(s):

`Move-Item {{path\to\source_key1 , path\to\source_key2 ...}} {{path\to\new_or_existing_key}}`

- Do not prompt for confirmation before overwriting existing files or registry keys:

`mv -Force {{path\to\source}} {{path\to\target}}`

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -Confirm {{path\to\source}} {{path\to\target}}`

- Move files in dry-run mode, showing files and directories which could be moved without executing them:

`mv -WhatIf {{path\to\source}} {{path\to\target}}`
