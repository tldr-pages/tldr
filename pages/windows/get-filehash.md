# Get-FileHash

> Calculate and display a file's hash.
> More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Calculate a hash for a specified file using the SHA256 algorithm:

`Get-FileHash {{path/to/file}}`

- Get a file's hash using the SHA1, SHA256, SHA384, SHA512, or MD5 algorithm:

`Get-FileHash {{path/to/file}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
