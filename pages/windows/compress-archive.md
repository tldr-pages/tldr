# Compress-Archive

> A cmdlet in PowerShell is used to create compressed (zipped) archive files.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive>.

- Compress a single file:

`Compress-Archive -Path "{{path\to\file.txt}}" -DestinationPath "{{path\to\file.zip}}"`

- Compress Multiple Files:

`Compress-Archive -Path "{{path\to\file1.txt}}", "{{path\to\file2.txt}}" -DestinationPath "{{path\to\files.zip}}"`

- Compress a Folder:

`Compress-Archive -Path "{{path\to\folder}}" -DestinationPath "{{path\to\folder.zip}}"`

- Update an existing archive:

`Compress-Archive -Path "{{path\to\file.txt}}" -DestinationPath "{{path\to\Folder.zip}}" -Update`

- Set compression level:

`Compress-Archive -Path "{{path\to\folder}}" -DestinationPath "{{path\to\folder.zip}}" -CompressionLevel {{Optimal | Fastest | NoCompression}}`
