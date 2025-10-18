# Expand-Archive

> A cmdlet in PowerShell is used to extract files from a compressed archive.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/expand-archive>.i

- Extract a ZIP file to a folder:

`Expand-Archive -Path "{{C:\Files\example.zip}}" -DestinationPath "{{C:\ExtractedFiles}}"`

- Overwrite existing files:

`Expand-Archive -Path "{{C:\Files\example.zip}}" -DestinationPath "{{C:\ExtractedFiles}}" -Force`

- Preview without Extracting:

`Expand-Archive -Path "{{C:\Files\example.zip}}" -DestinationPath "{{C:\ExtractedFiles}}" -WhatIf`

