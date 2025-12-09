# Compress-Archive

> A cmdlet in PowerShell is used to create compressed (zipped) archive files.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive>.

- Compress a single file:

`Compress-Archive -Path {{path\to\file.txt}} -DestinationPath {{path\to\file.zip}}`

- Compress multiple files:

`Compress-Archive -Path {{path\to\file1, path\to\file2, ...}} -DestinationPath {{path\to\files.zip}}`

- Compress a directory:

`Compress-Archive -Path {{path\to\directory}} -DestinationPath {{path\to\directory.zip}}`

- Update an existing archive:

`Compress-Archive -Path {{path\to\file}} -DestinationPath {{path\to\directory.zip}} -Update`

- Set compression level:

`Compress-Archive -Path {{path\to\directory}} -DestinationPath {{path\to\directory.zip}} -CompressionLevel {{Optimal|Fastest|NoCompression}}`
