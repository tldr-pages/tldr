# Compress-Archive

> A cmdlet in PowerShell used to create compressed (zipped) archive files
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive>

- Compress a Single File

`Compress-Archive -Path "{{C:\Example\File.txt}}" -DestinationPath "{{C:\Example\File.zip}}"`

- Compress Multiple Files

`Compress-Archive -Path "{{C:\Example\File1.txt}}", "{{C:\Example\File2.txt}}" -DestinationPath "{{C:\Example\Files.zip}}"`

- Compress a Folder

`Compress-Archive -Path "{{C:\Example\Folder}}" -DestinationPath "{{C:\Example\Folder.zip}}"`

- Update an existing archive

`Compress-Archive -Path "{{C:\Example\NewFile.txt}}" -DestinationPath "{{C:\Example\Folder.zip}}" -Update`

- Set compression level

`Compress-Archive -Path "{{C:\Example\Folder}}" -DestinationPath "{{C:\Example\Folder.zip}}" -CompressionLevel {{Optimal | Fastest | NoCompression}}`
