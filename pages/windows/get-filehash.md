# Get-FileHash

> Calculate a hash for a file.
> This command can only be used through PowerShell.
> More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Calculate a hash for a specified file using the SHA256 algorithm:

`Get-FileHash {{path/to/file}}`

- Calculate a hash for a specified file using a specified algorithm:

`Get-FileHash {{path/to/file}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
