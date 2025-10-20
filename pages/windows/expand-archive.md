# Expand-Archive

> A cmdlet in PowerShell is used to extract files from a compressed archive.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/expand-archive>.

- Extract a ZIP file to a folder:

`Expand-Archive -Path {{path\to\example.zip}} -DestinationPath {{path\to\extracted_files}}`

- Overwrite existing files:

`Expand-Archive -Path {{path\to\example.zip}} -DestinationPath {{path\to\extracted_files}} -Force`

- Preview without extracting:

`Expand-Archive -Path {{path\to\example.zip}} -DestinationPath {{path\to\extracted_files}} -WhatIf`
